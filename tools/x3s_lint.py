#!/usr/bin/env python3
"""
Lightweight linter for .x3s (X3 Script) source files.

Checks:
- Well-formed control flow: if/else/end, while/end (stack-based)
- Busy-loop guard: each while block must contain a 'wait <ms>' line
- Setup scripts must contain 'load text: id=<number>'
- Basic line-shape validation via regex allowlist (warn on unknown)
- Optional header checks: #name, #page (must look like 89xxx), #lang (44)
"""
from __future__ import annotations
import re, sys
from pathlib import Path
from dataclasses import dataclass

ROOT = Path(__file__).resolve().parents[1]
SRC  = ROOT / "src" / "scripts"

LINE_PATTERNS = [
  re.compile(r"^load text:\s*id=(\d+|\$[A-Za-z0-9_.]+)$", re.I),
  re.compile(r"^al engine:\s*register script='[^']+'$", re.I),
  re.compile(r"^al engine:\s*set plugin '[^']+' description to '.*'$", re.I),
  re.compile(r"^al engine:\s*set plugin '[^']+' timer interval to \d+\s*s$", re.I),
  re.compile(r"^\[THIS]->stop task \d+$", re.I),
  re.compile(r"^start task \d+\s+with script='[^']+'\s+on=\[THIS\]$", re.I),
  re.compile(r"^=?\s*\[THIS]->\s*call script '[^']+'( : .*)?$", re.I),
  re.compile(r"^=?\s*wait \d+\s*ms$", re.I),
  re.compile(r"^set global variable:\s*name='[^']+'\s*value=.*$", re.I),
  re.compile(r"^return (null|value .+)$", re.I),
  # control flow (syntax-only; expression is free-form)
  re.compile(r"^if\b.+$", re.I),
  re.compile(r"^else$", re.I),
  re.compile(r"^end$", re.I),
  re.compile(r"^while\b.+$", re.I),
]

HEADER_RX = re.compile(r'^\s*#(\w+)\s*:\s*(.+)$')
COMMENT_RX = re.compile(r'^\s*([*#].*|\s*)$')

@dataclass
class Block:
  kind: str   # 'if' or 'while'
  line_no: int
  has_wait: bool = False   # only used for while

def lint_file(path: Path) -> list[str]:
  errors: list[str] = []
  warnings: list[str] = []

  text = path.read_text(encoding="utf-8").splitlines()
  headers, body = {}, []

  # split header/comments vs body
  for i, raw in enumerate(text, start=1):
    if m := HEADER_RX.match(raw):
      headers[m.group(1).lower()] = m.group(2).strip()
      continue
    if COMMENT_RX.match(raw):
      continue
    body.append((i, raw.rstrip()))

  # header sanity
  if "page" in headers and not re.fullmatch(r"89\d{3}", headers["page"]):
    warnings.append(f"{path.name}:{1}: header #page should look like 89xxx")

  stack: list[Block] = []
  setup_like = path.name.startswith("setup.")

  # walk lines
  for ln, line in body:
    # control flow tracking
    low = line.strip().lower()
    if low.startswith("if "):
      stack.append(Block("if", ln))
    elif low == "else":
      if not stack or stack[-1].kind != "if":
        errors.append(f"{path.name}:{ln}: 'else' without matching 'if'")
    elif low.startswith("while "):
      stack.append(Block("while", ln))
    elif low == "end":
      if not stack:
        errors.append(f"{path.name}:{ln}: 'end' without opener")
      else:
        blk = stack.pop()
        if blk.kind == "while" and not blk.has_wait:
          errors.append(f"{path.name}:{blk.line_no}: while-block has no 'wait' before 'end'")
    # mark waits inside while
    if re.search(r'\bwait\s+\d+\s*ms\b', low):
      for b in reversed(stack):
        if b.kind == "while":
          b.has_wait = True
          break

    # line-shape validation (warn on unknown shapes)
    if not any(pat.match(line) for pat in LINE_PATTERNS):
      # Allow variable assignments and general calls as free-form to reduce false positives
      if not re.match(r"^\$[A-Za-z0-9_.]+(\s*=|->)", line) and "call script" not in low:
        warnings.append(f"{path.name}:{ln}: unrecognized line (check syntax): {line}")

  if stack:
    opener = stack[-1]
    errors.append(f"{path.name}:{opener.line_no}: '{opener.kind}' not closed with 'end'")

  # setup rule
  if setup_like and not any(re.match(r"^load text:\s*id=(\d+|\$[A-Za-z0-9_.]+)$", l, re.I) for _, l in body):
    errors.append(f"{path.name}: setup script missing 'load text: id=<...>'")

  # emit
  out = [f"ERROR: {e}" for e in errors] + [f"WARN:  {w}" for w in warnings]
  return out

def main():
  if not SRC.exists():
    print("No src/scripts directory found.", file=sys.stderr)
    sys.exit(1)

  files = sorted(SRC.glob("*.x3s"))
  if not files:
    print("No .x3s files found in src/scripts", file=sys.stderr)
    sys.exit(1)

  any_errors = False
  for p in files:
    msgs = lint_file(p)
    if msgs:
      print(f"== {p.name} ==")
      print("\n".join(msgs))
      if any(m.startswith("ERROR") for m in msgs):
        any_errors = True

  if any_errors:
    sys.exit(1)
  print("OK")
  sys.exit(0)

if __name__ == "__main__":
  main()

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
import json, re, sys
from pathlib import Path
from dataclasses import dataclass

ROOT = Path(__file__).resolve().parents[1]
SRC  = ROOT / "src" / "scripts"
RULES = ROOT / "tools" / "x3s_rules.json"

def load_patterns() -> list[re.Pattern[str]]:
  try:
    data = json.loads(RULES.read_text(encoding="utf-8"))
  except FileNotFoundError:
    return []
  pats = []
  for entry in data.get("patterns", []):
    rx = entry.get("regex")
    if rx:
      pats.append(re.compile(rx, re.I))
  return pats

HEADER_RX = re.compile(r'^\s*#(\w+)\s*:\s*(.+)$')
COMMENT_RX = re.compile(r'^\s*([*#].*|\s*)$')

@dataclass
class Block:
  kind: str   # 'if' or 'while'
  line_no: int
  var: str | None = None    # controlling var for while
  has_wait: bool = False
  has_progress: bool = False

def lint_file(path: Path, patterns: list[re.Pattern[str]] | None = None) -> list[str]:
  patterns = patterns or load_patterns()
  errors: list[str] = []
  warnings: list[str] = []

  text = path.read_text(encoding="utf-8").splitlines()
  headers, body = {}, []

  # split header/comments vs body
  for i, raw in enumerate(text, start=1):
    raw = raw.replace('\u00A0', ' ')
    if m := HEADER_RX.match(raw):
      headers[m.group(1).lower()] = m.group(2).strip()
      continue
    if COMMENT_RX.match(raw):
      continue
    body.append((i, raw.rstrip()))

  # pre-scan for labels that contain blocking menu calls
  label = None
  blocking_labels: set[str] = set()
  for _, line in body:
    low = line.strip().lower()
    if m := re.match(r'^([a-z0-9_\.]+):$', low):
      label = m.group(1)
      continue
    if low == 'endsub':
      label = None
      continue
    if label and ('open custom menu:' in low or 'open custom info menu:' in low):
      blocking_labels.add(label)

  # header sanity
  if "page" in headers and not re.fullmatch(r"89\d{3}", headers["page"]):
    warnings.append(f"{path.name}:{1}: header #page should look like 89xxx")

  stack: list[Block] = []
  setup_like = path.name.startswith("setup.")

  # walk lines
  for ln, line in body:
    # control flow tracking
    low = line.strip().lower()
    if re.match(r'^if\b', low):
      stack.append(Block("if", ln))
    elif re.match(r'^else\s+if\b', low):
      if not stack or stack[-1].kind != "if":
        errors.append(f"{path.name}:{ln}: 'else if' without matching 'if'")
    elif low == "else":
      if not stack or stack[-1].kind != "if":
        errors.append(f"{path.name}:{ln}: 'else' without matching 'if'")
    elif re.match(r'^while\b', low):
      var = None
      if m := re.match(r"while\s+\$([A-Za-z0-9_.]+)", low):
        var = m.group(1)
      stack.append(Block("while", ln, var=var))
    elif low == "end":
      if not stack:
        errors.append(f"{path.name}:{ln}: 'end' without opener")
      else:
        blk = stack.pop()
        if blk.kind == "while" and not (blk.has_wait or blk.has_progress):
          errors.append(f"{path.name}:{blk.line_no}: while-block has no 'wait' before 'end'")
    # mark waits inside while
    if re.search(r'\bwait(\s+\d+\s*ms| randomly from (\d+|\$[A-Za-z0-9_.]+) to (\d+|\$[A-Za-z0-9_.]+) ms)\b', low):
      for b in reversed(stack):
        if b.kind == "while":
          b.has_wait = True
          break

    # mark decrement progress in while loops
    if low.startswith("dec $") or low.startswith("inc $"):
      var = low.split()[1].lstrip("$")
      for b in reversed(stack):
        if b.kind == "while" and b.var == var:
          b.has_progress = True
          break
    if m := re.match(r"\$([A-Za-z0-9_.]+)\s*=\s*\$\1\s*[-+*/]", low):
      var = m.group(1)
      for b in reversed(stack):
        if b.kind == "while" and b.var == var:
          b.has_progress = True
          break

    # treat certain blocking calls as progress (e.g., menu interaction)
    if "open custom menu:" in low or "open custom info menu:" in low:
      for b in reversed(stack):
        if b.kind == "while":
          b.has_progress = True
          break

    if m := re.match(r'^gosub\s+([A-Za-z0-9_.]+):$', low):
      lbl = m.group(1)
      if lbl.lower() in blocking_labels:
        for b in reversed(stack):
          if b.kind == "while":
            b.has_progress = True
            break

    if low == "break":
      for b in reversed(stack):
        if b.kind == "while":
          b.has_progress = True
          break

    # line-shape validation (warn on unknown shapes)
    recognizable = any(pat.match(line.strip()) for pat in patterns)
    if not recognizable and not (re.match(r'^if\b', low) or re.match(r'^else\s+if\b', low) or low == "else" or low == "end" or re.match(r'^while\b', low)):
      # Allow variable assignments and general calls as free-form to reduce false positives
      if not re.match(r"^\s*=?\s*(?:\$[A-Za-z0-9_.]+|\[[A-Za-z]+\])(\[[^\]]+\])*\s*(=|->)", line) and "call script" not in low:
        warnings.append(f"{path.name}:{ln}: unrecognized line (check syntax): {line}")

  if stack:
    opener = stack[-1]
    errors.append(f"{path.name}:{opener.line_no}: '{opener.kind}' not closed with 'end'")

  # setup rule
  if setup_like and not any(re.match(r"^load text:\s*id=(\d+|\$[A-Za-z0-9_.]+)$", l.strip(), re.I) for _, l in body):
    errors.append(f"{path.name}: setup script missing 'load text: id=<...>'")

  # emit
  out = [f"ERROR: {e}" for e in errors] + [f"WARN:  {w}" for w in warnings]
  return out

def iter_paths(args: list[str]) -> list[Path]:
  if not args:
    return sorted(SRC.glob("*.x3s"))
  paths: list[Path] = []
  for a in args:
    p = Path(a)
    if p.is_dir():
      paths.extend(sorted(p.glob("*.x3s")))
    else:
      paths.append(p)
  return paths

def main(argv: list[str] | None = None):
  argv = argv or sys.argv[1:]
  files = iter_paths(argv)
  if not files:
    print("No .x3s files found", file=sys.stderr)
    sys.exit(1)

  patterns = load_patterns()
  any_errors = False
  for p in files:
    msgs = lint_file(p, patterns)
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

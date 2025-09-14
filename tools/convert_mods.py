#!/usr/bin/env python3
"""
Convert fixtures from tools/fixtures/mods/<mod_name>/
to tools/fixtures/known_good/<mod_name>/.

- scripts/*.xml with <codearray><line>…</line></codearray> → src/scripts/*.x3s
- t/*.xml copied verbatim
- director/** copied verbatim
- README.md per mod with a brief summary
"""

from __future__ import annotations
import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET


def _norm_path(p: str) -> Path:
    """Return a Path with Windows separators normalized.

    If the resulting absolute path does not exist, attempt to treat the input as
    relative to the current working directory.  This allows callers to pass in
    Windows-style paths like ``\\tools\\fixtures\\mods\\Foo`` even on POSIX
    systems.
    """

    candidate = Path(p.replace("\\", "/"))
    if candidate.exists():
        return candidate.resolve()
    if str(candidate).startswith("/"):
        candidate = Path.cwd() / str(candidate).lstrip("/")
        if candidate.exists():
            return candidate.resolve()
    return (Path.cwd() / candidate).resolve()

RE_LOAD_TEXT = re.compile(r"load text:\s*id\s*=\s*(\d+)", re.IGNORECASE)

@dataclass
class ModSummary:
    scripts_converted: int = 0
    scripts_skipped: int = 0
    t_copied: int = 0
    director_copied: bool = False
    notes: list[str] = None

    def __post_init__(self):
        if self.notes is None:
            self.notes = []

def discover_mods(mods_root: Path) -> list[Path]:
    return sorted([p for p in mods_root.iterdir() if p.is_dir()])

def ensure_dirs(out_root: Path, mod_name: str) -> dict[str, Path]:
    base = out_root / mod_name
    paths = {
        "base": base,
        "scripts": base / "src" / "scripts",
        "t": base / "t",
        "director": base / "director",
    }
    for p in paths.values():
        p.mkdir(parents=True, exist_ok=True)
    return paths

def is_x3_script_xml(xml_path: Path) -> bool:
    try:
        root = ET.parse(xml_path).getroot()
    except ET.ParseError:
        return False

    tag = root.tag.lower()
    if tag == "codearray":
        return any(ch.tag.lower() == "line" for ch in root)
    if tag == "script":
        st = root.find("sourcetext")
        if st is not None:
            return any(ch.tag.lower() == "line" for ch in st)
    return False

def extract_lines(xml_path: Path) -> list[str]:
    root = ET.parse(xml_path).getroot()

    tag = root.tag.lower()
    if tag == "codearray":
        line_nodes = [n for n in root if n.tag.lower() == "line"]
    elif tag == "script":
        st = root.find("sourcetext")
        if st is None:
            return []
        line_nodes = [n for n in st if n.tag.lower() == "line"]
    else:
        return []

    lines: list[str] = []
    for node in line_nodes:
        # node.text may include a leading newline; strip it but preserve indentation
        text = (node.text or "").replace("\n", "")
        for child in node:
            text += "".join(child.itertext())
        lines.append(text.rstrip())
    return lines

def detect_page_id(lines: list[str]) -> str | None:
    for ln in lines:
        m = RE_LOAD_TEXT.search(ln)
        if m:
            return m.group(1)
    return None

def has_lang_44(t_dir: Path) -> bool:
    if not t_dir.exists():
        return False
    return any("-L044" in p.name for p in t_dir.glob("*.xml"))

def write_x3s(out_path: Path, header: dict[str, str], lines: list[str]) -> None:
    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        # Header (only write keys that exist)
        for key in ("name", "page", "lang", "origin_mod", "source"):
            if key in header and header[key]:
                f.write(f"#{key}: {header[key]}\n")
        f.write("\n")
        # Write exactly one line for each XML <line> node
        for line in lines:
            f.write(line.rstrip() + "\n")

def copy_tree(src: Path, dst: Path, summary: ModSummary) -> None:
    if not src.exists():
        return
    # Copy files preserving times; keep directory structure
    for p in src.rglob("*"):

        rel = p.relative_to(src)
        target = dst / rel
        if p.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, target)
            if src.name == "t":
                summary.t_copied += 1

def convert_mod(mod_dir: Path, out_root: Path) -> ModSummary:
    mod_name = mod_dir.name
    paths = ensure_dirs(out_root, mod_name)
    summary = ModSummary()

    # Copy text pages and director first (so we can infer #lang)
    copy_tree(mod_dir / "t", paths["t"], summary)
    has_44 = has_lang_44(paths["t"])
    if (mod_dir / "director").exists():
        copy_tree(mod_dir / "director", paths["director"], summary)
        summary.director_copied = True

    # Convert each scripts/*.xml that is an X3 script
    scripts_src = mod_dir / "scripts"
    if scripts_src.exists():
        for p in sorted(scripts_src.iterdir()):
            if not p.is_file():
                continue
            if p.suffix.lower() != ".xml":
                summary.scripts_skipped += 1
                summary.notes.append(f"Skipped non-XML file: {p.name}")
                continue
            if not is_x3_script_xml(p):
                summary.scripts_skipped += 1
                summary.notes.append(f"Skipped non-X3Script XML: {p.name}")
                continue

            lines = extract_lines(p)
            page = detect_page_id(lines)
            header = {
                "name": p.stem,                # plugin.slx.foo
                "origin_mod": mod_name,
                "source": f"mods/{mod_name}/{p.relative_to(mod_dir)}",
            }
            if page:
                header["page"] = page
            if has_44:
                header["lang"] = "44"

            out_path = paths["scripts"] / f"{p.stem}.x3s"
            write_x3s(out_path, header, lines)
            summary.scripts_converted += 1
    else:
        summary.notes.append("No scripts/ directory found in mod")

    # README with summary
    write_readme(paths["base"], mod_name, summary)
    return summary

def write_readme(base_dir: Path, mod_name: str, s: ModSummary) -> None:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    readme = base_dir / "README.md"
    lines = [
        f"# {mod_name} (fixtures)",
        "",
        f"Generated from `mods/{mod_name}` on {timestamp}.",
        "",
        "## Summary",
        f"- Scripts converted: {s.scripts_converted}",
        f"- Scripts skipped:  {s.scripts_skipped}",
        f"- Text pages copied: {s.t_copied}",
        f"- Director copied:   {'yes' if s.director_copied else 'no'}",
    ]
    if s.notes:
        lines += ["", "## Notes"] + [f"- {n}" for n in s.notes]
    readme.write_text("\n".join(lines) + "\n", encoding="utf-8")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert known_good mods to per-mod .x3s fixtures."
    )
    parser.add_argument(
        "--single-mod",
        help="Convert only this mod directory",
    )
    parser.add_argument(
        "--mods-dir",
        default=str(Path("tools/fixtures/mods")),
        help="Input mods/ root (default: tools/fixtures/mods)",
    )
    parser.add_argument(
        "--out-dir",
        default=str(Path("tools/fixtures/known_good")),
        help="Output root (default: tools/fixtures/known_good)",
    )
    return parser.parse_args()

def main() -> int:
    args = parse_args()
    out_root = _norm_path(args.out_dir)

    if args.single_mod:
        mod_dir = _norm_path(args.single_mod)
        if not mod_dir.exists():
            print(f"ERROR: mod path not found: {mod_dir}", file=sys.stderr)
            return 2
        mods = [mod_dir]
        print(f"Converting from {mod_dir} -> {out_root}")
    else:
        mods_root = _norm_path(args.mods_dir)
        if not mods_root.exists():
            print(f"ERROR: mods root not found: {mods_root}", file=sys.stderr)
            return 2
        mods = discover_mods(mods_root)
        if not mods:
            print(f"ERROR: no mod folders in {mods_root}", file=sys.stderr)
            return 2
        print(f"Converting from {mods_root} -> {out_root}")

    total = ModSummary()
    failed_mods: list[str] = []
    for mod in mods:
        print(f"- [{mod.name}] …", end="", flush=True)
        s = convert_mod(mod, out_root)
        print(
            f" converted={s.scripts_converted} skipped={s.scripts_skipped} t={s.t_copied} director={'y' if s.director_copied else 'n'}"
        )
        if (mod / "scripts").exists() and s.scripts_converted == 0:
            failed_mods.append(mod.name)
        total.scripts_converted += s.scripts_converted
        total.scripts_skipped += s.scripts_skipped
        total.t_copied += s.t_copied
        total.notes.extend((s.notes or []))

    print("\nDone.")
    print(f"Total scripts converted: {total.scripts_converted}")
    print(f"Total scripts skipped:  {total.scripts_skipped}")
    print(f"Total t files copied:   {total.t_copied}")
    if failed_mods:
        print(
            "ERROR: no scripts converted for mods with scripts/: "
            + ", ".join(failed_mods),
            file=sys.stderr,
        )
        return 1
    return 0 if total.scripts_converted > 0 else 1

if __name__ == "__main__":
    sys.exit(main())

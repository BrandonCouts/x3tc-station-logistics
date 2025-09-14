#!/usr/bin/env python3
"""Convert mod fixtures to per-mod .x3s folders."""
import sys, re, shutil, datetime
from pathlib import Path
import xml.etree.ElementTree as ET
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
MODS_ROOT = ROOT / 'tools' / 'fixtures' / 'known_good' / 'mods'
OUT_ROOT = ROOT / 'tools' / 'fixtures' / 'known_good'

spec = importlib.util.spec_from_file_location('x3s_lint', ROOT / 'tools' / 'x3s_lint.py')
x3s_lint = importlib.util.module_from_spec(spec)
sys.modules['x3s_lint'] = x3s_lint
spec.loader.exec_module(x3s_lint)

LOAD_TEXT_RX = re.compile(r"load text: id=(\d+)", re.I)


def convert_script(mod_name: str, src: Path, dest: Path, has_lang44: bool) -> tuple[bool, int | None]:
    """Convert a single script XML file to .x3s.

    Returns (converted, page_id).
    """
    try:
        tree = ET.parse(src)
    except ET.ParseError:
        return False, None
    root = tree.getroot()
    if root.tag == 'codearray':
        line_elems = root.findall('line')
    elif root.tag == 'script':
        st = root.find('sourcetext')
        if st is None:
            return False, None
        line_elems = st.findall('line')
    else:
        return False, None

    lines = []
    page_id = None
    for elem in line_elems:
        text = ''.join(elem.itertext())
        text = text.rstrip()
        lines.append(text)
        if page_id is None:
            m = LOAD_TEXT_RX.search(text)
            if m:
                page_id = m.group(1)

    header = [f"#name: {src.stem}"]
    if page_id:
        header.append(f"#page: {page_id}")
    if has_lang44:
        header.append("#lang: 44")
    header.append(f"#origin_mod: {mod_name}")
    header.append(f"#source: mods/{mod_name}/scripts/{src.name}")

    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open('w', encoding='utf-8', newline='\n') as f:
        for h in header:
            f.write(h + '\n')
        for line in lines:
            f.write(line.rstrip() + '\n')
    return True, page_id


def copy_tree(src: Path, dst: Path) -> int:
    count = 0
    if not src.exists():
        return 0
    for p in src.rglob('*'):
        rel = p.relative_to(src)
        target = dst / rel
        if p.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, target)
            count += 1
    return count


def convert_mod(mod_dir: Path) -> dict:
    mod_name = mod_dir.name
    print(f"[mod {mod_name}]")
    dest_root = OUT_ROOT / mod_name
    scripts_src = mod_dir / 'scripts'
    t_src = mod_dir / 't'
    director_src = mod_dir / 'director'

    dest_scripts = dest_root / 'src' / 'scripts'
    dest_t = dest_root / 't'
    dest_director = dest_root / 'director'

    dest_scripts.mkdir(parents=True, exist_ok=True)
    dest_t.mkdir(parents=True, exist_ok=True)

    has_lang44 = any(p.name.endswith('L044.xml') for p in t_src.glob('*-L*.xml')) if t_src.exists() else False

    converted = 0
    skipped = []
    if scripts_src.exists():
        for src in sorted(scripts_src.iterdir()):
            if src.suffix.lower() != '.xml':
                skipped.append(src.name)
                continue
            out_file = dest_scripts / f"{src.stem}.x3s"
            ok, _ = convert_script(mod_name, src, out_file, has_lang44)
            if ok:
                msgs = x3s_lint.lint_file(out_file)
                if any(m.startswith('ERROR') for m in msgs):
                    out_file.unlink(missing_ok=True)
                    skipped.append(f"{src.name} (lint failed)")
                else:
                    converted += 1
            else:
                skipped.append(src.name)
    if scripts_src.exists() and converted == 0:
        raise RuntimeError(f"no scripts converted for mod {mod_name}")

    pages = 0
    if t_src.exists():
        for tf in sorted(t_src.glob('*-L*.xml')):
            shutil.copy2(tf, dest_t / tf.name)
            pages += 1

    director_files = copy_tree(director_src, dest_director)

    date = datetime.date.today().isoformat()
    readme = dest_root / 'README.md'
    lines = [
        f"Generated from mods/{mod_name} on {date}",
        '',
        f"Scripts converted: {converted}",
        f"Text pages copied: {pages}",
    ]
    if director_files:
        lines.append(f"Director files copied: {director_files}")
    if skipped:
        lines.append('Skipped files:')
        for s in skipped:
            lines.append(f"- {s}")
    readme.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    return {'scripts': converted, 'pages': pages, 'skipped': skipped}


def main():
    if not MODS_ROOT.exists():
        print(f"mods path not found: {MODS_ROOT}", file=sys.stderr)
        sys.exit(1)
    any_fail = False
    for mod_dir in sorted(p for p in MODS_ROOT.iterdir() if p.is_dir()):
        try:
            summary = convert_mod(mod_dir)
            print(f"  converted {summary['scripts']} scripts, {summary['pages']} pages")
        except Exception as e:
            any_fail = True
            print(f"  ERROR: {e}")
    if any_fail:
        sys.exit(1)

if __name__ == '__main__':
    main()

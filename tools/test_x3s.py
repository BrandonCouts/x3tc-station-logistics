#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def run(cmd):
  print('>', ' '.join(cmd))
  p = subprocess.run(cmd, cwd=ROOT)
  if p.returncode:
    sys.exit(p.returncode)


def run_fail(cmd):
  print('>', ' '.join(cmd))
  p = subprocess.run(cmd, cwd=ROOT)
  if p.returncode == 0:
    print('expected failure but command passed')
    sys.exit(1)


if __name__ == '__main__':
  # Convert only the OKTraders1_7_1 mod using a Windows-style path
  run([
      sys.executable,
      'tools/convert_mods.py',
      '--single-mod', r'\tools\fixtures\mods\OKTraders1_7_1',
      '--out-dir', 'tools/fixtures/known_good',
  ])

  # Verify that XML <line> count equals body line count in each .x3s
  mod_name = 'OKTraders1_7_1'
  xml_dir = ROOT / 'tools/fixtures/mods' / mod_name / 'scripts'
  x3s_dir = ROOT / 'tools/fixtures/known_good' / mod_name / 'src/scripts'
  for xml_path in sorted(xml_dir.glob('*.xml')):
    root = ET.parse(xml_path).getroot()
    tag = root.tag.lower()
    if tag == 'script':
      st = root.find('sourcetext')
      if st is None:
        continue
      line_nodes = [n for n in st if n.tag.lower() == 'line']
    elif tag == 'codearray':
      line_nodes = [n for n in root if n.tag.lower() == 'line']
    else:
      continue

    x3s_path = x3s_dir / (xml_path.stem + '.x3s')
    with x3s_path.open(encoding='utf-8') as f:
      lines = f.read().splitlines()
    i = 0
    while i < len(lines) and lines[i].startswith('#'):
      i += 1
    if i < len(lines) and lines[i] == '':
      i += 1
    body_lines = lines[i:]
    if len(line_nodes) != len(body_lines):
      print(
          f'line count mismatch for {xml_path.name}: '
          f'xml={len(line_nodes)} x3s={len(body_lines)}'
      )
      sys.exit(1)

  # lint project scripts
  run([sys.executable, 'tools/x3s_lint.py', 'src/scripts'])

  # lint known-good fixtures recursively (best effort)
  good_paths = sorted(ROOT.glob('tools/fixtures/known_good/**/src/scripts/*.x3s'))
  if good_paths:
    cmd = [sys.executable, 'tools/x3s_lint.py', *[str(p.relative_to(ROOT)) for p in good_paths]]
    print('>', ' '.join(cmd))
    subprocess.run(cmd, cwd=ROOT)

  # ensure safety checks still trigger (negative tests)
  fail_paths = sorted((ROOT / 'tools/fixtures/should_fail').glob('**/*.x3s'))
  if fail_paths:
    run_fail([sys.executable, 'tools/x3s_lint.py', *[str(p.relative_to(ROOT)) for p in fail_paths]])

from pathlib import Path
import subprocess, sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def extract_xml_lines(xml_path: Path) -> list[str]:
  root = ET.parse(xml_path).getroot()
  tag = root.tag.lower()
  if tag == 'codearray':
    line_nodes = [n for n in root if n.tag.lower() == 'line']
  elif tag == 'script':
    st = root.find('sourcetext')
    if st is None:
      return []
    line_nodes = [n for n in st if n.tag.lower() == 'line']
  else:
    return []

  lines: list[str] = []
  for node in line_nodes:
    text = (node.text or '').replace('\n', '')
    for child in node:
      text += ''.join(child.itertext())
    lines.append(text.rstrip())
  return lines


def read_x3s_body(x3s_path: Path) -> list[str]:
  lines = x3s_path.read_text(encoding='utf-8').splitlines()
  body_started = False
  body: list[str] = []
  for ln in lines:
    if not body_started:
      if ln.strip() == '':
        body_started = True
      continue
    body.append(ln)
  return body

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
  mods_dir = ROOT / 'tools/fixtures/mods'
  ads_real = mods_dir / 'ads'
  ads_symlink = mods_dir / 'ADS'
  if not ads_symlink.exists():
    ads_symlink.symlink_to(ads_real, target_is_directory=True)

  # Run the converter for the ADS mod using a Windows-style path
  run([sys.executable, 'tools/convert_mods.py', '--single-mod', '\\tools\\fixtures\\mods\\ADS', '--out-dir', 'tools/fixtures/known_good'])

  # Validate line counts between XML and generated .x3s files
  ads_xml_dir = ads_real / 'scripts'
  ads_out_dir = ROOT / 'tools/fixtures/known_good/ADS/src/scripts'
  for x3s_path in sorted(ads_out_dir.glob('*.x3s')):
    xml_path = ads_xml_dir / f'{x3s_path.stem}.xml'
    xml_lines = extract_xml_lines(xml_path)
    x3s_lines = read_x3s_body(x3s_path)
    assert len(xml_lines) == len(x3s_lines), f'line count mismatch for {x3s_path.name}'
    for src, out in zip(xml_lines, x3s_lines):
      if len(src) > 1:
        assert len(out) > 1, f'unexpected single-character line in {x3s_path.name}'

  src_files = sorted((ROOT / 'src/scripts').glob('*.x3s'))
  good_files = sorted(ROOT.glob('tools/fixtures/known_good/**/src/scripts/*.x3s'))
  fail_files = sorted(ROOT.glob('tools/fixtures/should_fail/**/*.x3s'))

  run([sys.executable, 'tools/x3s_lint.py', *[str(p.relative_to(ROOT)) for p in src_files + good_files]])
  if fail_files:
    run_fail([sys.executable, 'tools/x3s_lint.py', *[str(p.relative_to(ROOT)) for p in fail_files]])

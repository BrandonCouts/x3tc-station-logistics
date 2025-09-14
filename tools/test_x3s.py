from pathlib import Path
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> None:
  """Run a command expecting success."""
  print('>', ' '.join(cmd))
  subprocess.run(cmd, cwd=ROOT, check=True)


def run_fail(cmd: list[str]) -> None:
  """Run a command expecting non-zero exit status."""
  print('>', ' '.join(cmd))
  p = subprocess.run(cmd, cwd=ROOT)
  if p.returncode == 0:
    print('expected failure but command passed')
    sys.exit(1)


def known_good_dirs() -> list[str]:
  base = ROOT / 'tools/fixtures/known_good'
  dirs = {base}
  for p in base.rglob('*.x3s'):
    dirs.add(p.parent)
  return [str(d.relative_to(ROOT)) for d in sorted(dirs)]


if __name__ == '__main__':
  run([sys.executable, 'tools/x3s_lint.py', 'src/scripts', *known_good_dirs()])

  fail_dir = ROOT / 'tools/fixtures/should_fail'
  if list(fail_dir.rglob('*.x3s')):
    run_fail([sys.executable, 'tools/x3s_lint.py', str(fail_dir.relative_to(ROOT))])

  suite = unittest.defaultTestLoader.discover(str(ROOT / 'tools/tests'))
  result = unittest.TextTestRunner().run(suite)
  if not result.wasSuccessful():
    sys.exit(1)


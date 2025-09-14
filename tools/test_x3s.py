from pathlib import Path
import subprocess, sys

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
  src_files = sorted((ROOT / 'src/scripts').glob('*.x3s'))
  good_files = sorted(ROOT.glob('tools/fixtures/known_good/**/src/scripts/*.x3s'))
  fail_files = sorted(ROOT.glob('tools/fixtures/should_fail/**/*.x3s'))

  run([sys.executable, 'tools/x3s_lint.py', *[str(p.relative_to(ROOT)) for p in src_files + good_files]])
  if fail_files:
    run_fail([sys.executable, 'tools/x3s_lint.py', *[str(p.relative_to(ROOT)) for p in fail_files]])

#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path

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
  # lint project scripts
  run([sys.executable, 'tools/x3s_lint.py', 'src/scripts'])

  # lint known-good fixtures
  run([sys.executable, 'tools/x3s_lint.py', 'tools/fixtures/known_good'])

  # ensure safety checks still trigger
  run_fail([sys.executable, 'tools/x3s_lint.py', 'tools/fixtures/should_fail'])


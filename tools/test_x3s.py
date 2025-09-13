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
    sys.exit(1)

if __name__ == '__main__':
  run([sys.executable, 'tools/x3s_lint.py'])
  run([sys.executable, 'tools/x3s_lint.py', 'tools/fixtures/known_good'])
  run_fail([sys.executable, 'tools/x3s_lint.py', 'tools/fixtures/should_fail'])


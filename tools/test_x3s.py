from pathlib import Path
import json
import subprocess
import sys
import unittest

import x3s_lint as x3s_lint

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


class RuleExampleTests(unittest.TestCase):
  def test_rule_examples(self) -> None:
    data = json.loads((ROOT / 'tools/x3s_rules.json').read_text(encoding='utf-8'))
    pats = {r.name: r.regex for r in x3s_lint.load_patterns()}
    for rule in data.get('rules', []):
      rx = pats.get(rule['name'])
      self.assertIsNotNone(rx, rule['name'])
      for ex in rule.get('examples', []):
        self.assertRegex(ex, rx, f"example failed for {rule['name']}: {ex}")


class CoverageTests(unittest.TestCase):
  def test_known_good_coverage(self) -> None:
    patterns = x3s_lint.load_patterns()
    total = 0
    unrec = 0
    for p in (ROOT / 'tools/fixtures/known_good').rglob('*.x3s'):
      text = p.read_text(encoding='utf-8').splitlines()
      body = []
      for raw in text:
        raw = raw.replace('\u00A0', ' ')
        if x3s_lint.HEADER_RX.match(raw) or x3s_lint.COMMENT_RX.match(raw):
          continue
        body.append(raw.rstrip())
      total += len(body)
      out = x3s_lint.lint_file(p, patterns)
      unrec += sum(1 for line in out if 'unrecognized line' in line)
    coverage = 1.0 if total == 0 else 1 - (unrec / total)
    self.assertGreaterEqual(coverage, 0.95, f'coverage below 95%: {coverage:.2%}')


if __name__ == '__main__':
  run([sys.executable, 'tools/x3s_lint.py', 'src/scripts', *known_good_dirs()])

  fail_dir = ROOT / 'tools/fixtures/should_fail'
  if list(fail_dir.rglob('*.x3s')):
    run_fail([sys.executable, 'tools/x3s_lint.py', str(fail_dir.relative_to(ROOT))])

  suite = unittest.defaultTestLoader.discover(str(ROOT / 'tools/tests'))
  suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RuleExampleTests))
  suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(CoverageTests))
  result = unittest.TextTestRunner().run(suite)
  if not result.wasSuccessful():
    sys.exit(1)


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


class RuleExampleTests(unittest.TestCase):
  def test_rule_examples(self) -> None:
    data = json.loads((ROOT / 'tools/x3s_rules.json').read_text(encoding='utf-8'))
    pats = {r.name: r.regex for r in x3s_lint.load_patterns()}
    for rule in data.get('rules', []):
      rx = pats.get(rule['name'])
      self.assertIsNotNone(rx, rule['name'])
      for ex in rule.get('examples', []):
        self.assertRegex(ex, rx, f"example failed for {rule['name']}: {ex}")


def main() -> int:
  run([sys.executable, 'tools/x3s_lint.py', 'src/scripts'])

  suite = unittest.defaultTestLoader.discover(str(ROOT / 'tools/tests'))
  suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RuleExampleTests))
  result = unittest.TextTestRunner().run(suite)
  return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
  sys.exit(main())


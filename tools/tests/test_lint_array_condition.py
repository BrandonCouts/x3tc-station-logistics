import tempfile
from pathlib import Path
import sys
import unittest

# Ensure we can import x3s_lint from the tools directory
sys.path.append(str(Path(__file__).resolve().parents[1]))
import x3s_lint


class ArrayConditionTests(unittest.TestCase):
    def test_array_index_in_condition_disallowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad.x3s"
            p.write_text("if $arr[$i] > 0\nend\n", encoding="utf-8")
            msgs = x3s_lint.lint_file(p)
            self.assertTrue(
                any("array indices not allowed in conditionals" in m for m in msgs), msgs
            )


if __name__ == "__main__":
    unittest.main()

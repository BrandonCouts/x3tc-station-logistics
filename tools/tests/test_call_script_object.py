import tempfile
from pathlib import Path
import sys
import unittest

sys.path.append(str(Path(__file__).resolve().parents[1]))
import x3s_lint

class CallScriptObjectTests(unittest.TestCase):
    def test_missing_object_raises_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad.x3s"
            p.write_text("call script 'lib.slx.query' : function='GetSector', station=$st\n", encoding='utf-8')
            msgs = x3s_lint.lint_file(p)
            self.assertTrue(
                any("call script missing object reference" in m for m in msgs), msgs
            )

if __name__ == "__main__":
    unittest.main()

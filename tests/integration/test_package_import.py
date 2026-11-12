"""Integration test: the installed package imports cleanly from a fresh
interpreter, exactly as a fresh clone would use it.

Kept minimal on purpose: it asserts the public surface that exists today
(the package version) and that PyTorch is importable alongside it.
"""

import subprocess
import sys


def test_fresh_interpreter_imports_package() -> None:
    code = "import small_lab, torch; print(small_lab.__version__); print(torch.__version__)"
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.splitlines()[0] == "0.1.0"

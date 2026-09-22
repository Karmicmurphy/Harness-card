#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
subprocess.run(
    [sys.executable, str(ROOT / "workers" / "validate_authority_spine.py")],
    check=True,
)
print("Harness authority spine PASS")

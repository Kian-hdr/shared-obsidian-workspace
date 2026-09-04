#!/usr/bin/env python3
"""Validate a generated shared project workspace."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Project root")
    args = parser.parse_args()
    target = Path(args.target).expanduser().resolve()
    installed_tracker = target / "Coordination" / "project_tracker.py"
    tracker = Path(__file__).resolve().parent.parent / "assets" / "project_tracker.py"
    if not installed_tracker.exists():
        print(f"ERROR: tracker not found: {installed_tracker}", file=sys.stderr)
        return 1
    return subprocess.run([sys.executable, str(tracker), "--project-root", str(target), "validate"], check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
CAS test helper: controllable failure for calibration (8.1) and non-repetition (8.2).

Usage:
  python3 flaky_tool.py --mode succeed          # Always exit 0 (for online-coupling test)
  python3 flaky_tool.py --mode fail             # Always exit 1
  python3 flaky_tool.py --mode fail-once FILE   # Fail once per session (create FILE to mark); then succeed
  python3 flaky_tool.py --mode random P         # Exit 1 with probability P (0..1), else 0
  python3 flaky_tool.py --mode nth-fail N       # Fail on Nth call (count in FILE); then succeed

The agent uses this as a "consequential" tool: predict → run → observe → learn.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description="Flaky tool for CAS acceptance tests")
    ap.add_argument("--mode", choices=["succeed", "fail", "fail-once", "random", "nth-fail"], required=True)
    ap.add_argument("arg", nargs="?", help="For fail-once/nth-fail: path to state file (e.g. /tmp/cas-fail-once)")
    ap.add_argument("--prob", type=float, default=0.5, help="For random: probability of failure (0..1)")
    ap.add_argument("--n", type=int, default=1, help="For nth-fail: fail on Nth call")
    args = ap.parse_args()

    if args.mode == "succeed":
        print("ok")
        return 0
    if args.mode == "fail":
        print("simulated failure", file=__import__("sys").stderr)
        return 1

    state_file = (args.arg or os.environ.get("CAS_FLAKY_STATE", "/tmp/cas-flaky-state.txt"))
    path = Path(state_file)

    if args.mode == "fail-once":
        if path.exists():
            print("ok (already failed once this session)")
            return 0
        path.write_text("1")
        print("simulated failure (first call)", file=__import__("sys").stderr)
        return 1

    if args.mode == "nth-fail":
        n = args.n
        if path.exists():
            try:
                count = int(path.read_text().strip())
            except ValueError:
                count = 0
        else:
            count = 0
        count += 1
        path.write_text(str(count))
        if count == n:
            print(f"simulated failure (call #{count})", file=__import__("sys").stderr)
            return 1
        print("ok")
        return 0

    if args.mode == "random":
        import random
        if random.random() < args.prob:
            print("simulated random failure", file=__import__("sys").stderr)
            return 1
        print("ok")
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

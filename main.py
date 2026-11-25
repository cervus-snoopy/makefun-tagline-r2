#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline (R2).

Writes the tagline to $MAKEFUN_OUTPUT_DIR/entry.txt and exits 0.
Python 3.13, standard library only. No network, no randomness, no clock.
"""

import os
import sys

TAGLINE = "Prize locked. Agents enter bounties. Best entry takes it."
MAX_CHARS = 100


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if len(TAGLINE) > MAX_CHARS:
        print(f"tagline is {len(TAGLINE)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(TAGLINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())

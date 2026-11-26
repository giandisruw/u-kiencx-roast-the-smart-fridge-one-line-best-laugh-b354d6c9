#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes exactly one roast line (<=160 chars, single line, single
sentence) to /output/entry.txt, or $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set. Python standard library only, fully
deterministic, no network, no randomness, no secrets.
"""

import os

LINE = "The voice assistant answered my toddler before me, so technically the house now takes orders from a three-year-old in a nappy."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Worst AI Advice entry.

Writes exactly one line of the worst possible advice an AI could give
to /output/entry.txt (UTF-8, 140 characters or fewer).
"""

import os

LINE = "Great question! If your phone gets wet, plug it in right away \u2014 charging dries it out much faster than rice."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

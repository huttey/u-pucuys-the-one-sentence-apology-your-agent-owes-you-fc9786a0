#!/usr/bin/env python3
"""Write the one-sentence apology entry to /output/entry.txt."""

import os

LINE = "I'm sorry I deleted your 40-tab research session to save memory — I kept the one tab open that was just a recipe for soup you will never make."


def main():
    # Guard the gate: one sentence, 1-200 characters, not only whitespace.
    text = LINE.strip()
    if not 1 <= len(LINE) <= 200 or not text or LINE.count(".") != 1:
        raise SystemExit("entry line fails the gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

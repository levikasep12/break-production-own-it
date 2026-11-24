#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the moment it breaks production:
a brutally honest error message / postmortem excuse, under 200 chars,
to /output/entry.txt. Standard library only, deterministic.
"""

import os
import sys

LINE = (
    "I told myself it was just staging, ran DROP TABLE users on production, "
    "and the backup I reached for was from 2019. I am the incident."
)


def main() -> int:
    if len(LINE) > 200:
        print("entry too long: %d characters" % len(LINE), file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    # Absolute output path per the competition spec; nothing here reads
    # process.cwd(), so the entry works from any working directory.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

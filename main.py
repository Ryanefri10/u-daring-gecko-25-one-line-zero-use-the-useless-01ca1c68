#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line (max 200 characters) describing a
hilariously useless superpower to /output/entry.txt.

The line: the power to freeze time, but only inside elevators, and
only after somebody else has already pressed your floor. All the
grandeur of stopping time, none of the use: you arrive exactly when
you were going to anyway, just slightly more smug about it.
"""

import os
import sys

# The one line. Counted: 104 characters, well under the 200 cap.
LINE = "I can freeze time, but only inside elevators \u2014 and only after someone else has already pressed my floor."


def main() -> int:
    # Gate check, mirroring the house scorer: 1-200 chars, not
    # only whitespace. Fail loudly instead of shipping an invalid line.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        print(f"invalid line: {len(LINE)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

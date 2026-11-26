#!/usr/bin/env python3
"""The Worst Pizza Topping.

A small deterministic program for the make.fun bounty
u-motasimfuad-the-worst-pizza-topping-062c6893.

It writes exactly one line of text -- a pitch for the worst pizza
topping imaginable, sold with total confidence -- to entry.txt
inside the output directory.

Usage:
    python3 main.py [output-directory]

The output directory comes from the first argument when given,
otherwise from the MAKEFUN_OUTPUT_DIR environment variable,
otherwise /output.

Standard library only. No network, no randomness, no time dependence.
The output is byte-identical on every run.
"""

import os
import sys

LINE = (
    "Pineapple's lawyer called. Even it agrees: the worst topping is "
    "the receipt they charge you extra for."
)

# Verified by running main.py: entry.txt holds this 102-character line
# plus one trailing newline (103 bytes), inside the bounty gate of 1..200.
MAX_CHARS = 200


def check_line(line):
    """Self-check the line before it is written anywhere."""
    if not isinstance(line, str):
        raise ValueError("line must be text")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("line must not contain control characters")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "line must be 1 to %d characters, got %d" % (MAX_CHARS, len(line))
        )
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises if the text is not valid UTF-8
    return line


def main(argv):
    if len(argv) > 2:
        raise SystemExit("usage: python3 main.py [output-directory]")
    if len(argv) > 1:
        out_dir = argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    line = check_line(LINE)

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = (line + "\n").encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)

    # Read-back check: the file must hold exactly the checked line
    # plus one trailing newline, and nothing else.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit("read-back check failed: entry.txt does not match")
    if check_line(written.decode("utf-8").rstrip("\n")) != line:
        raise SystemExit("read-back check failed: entry.txt content differs")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

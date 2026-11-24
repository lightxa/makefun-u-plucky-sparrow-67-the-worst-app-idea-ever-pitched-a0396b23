#!/usr/bin/env python3
"""SockSync: the worst app idea ever pitched.

Writes one sentence (at most 240 characters) pitching the most
useless app imaginable to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The program validates the sentence
before writing it: it must be non-empty, at most 240 characters,
and exactly one sentence.
"""

import os
import sys

ENTRY = (
    "SockSync matches your single lost sock with a stranger's single "
    "lost sock and schedules weekly video calls, so two socks you will "
    "never wear again can stay in touch forever, with a premium tier "
    "for socks that want to meet in person."
)

MAX_CHARS = 240


def validate(text):
    """Check the entry against the competition gate and judge rules."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    # Exactly one sentence: a single terminal full stop, no other
    # sentence-ending punctuation anywhere in the text.
    terminators = sum(text.count(mark) for mark in (".", "!", "?"))
    if terminators != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")
    if "  " in text:
        raise ValueError("entry contains double spaces")


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), out_path))
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

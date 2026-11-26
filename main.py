#!/usr/bin/env python3
"""Museum of the Year 3000 — round 2 entry.

Writes one deadpan museum label, as written in the year 3000, beside an
ordinary object from today: the QR code menu. The joke is the ritual the
curator records without blinking — diners scanned a black-and-white square
to read the food list, then asked a human to read it aloud anyway.

The program is fully deterministic: no network, no clock, no randomness,
no environment input. It writes exactly one line of 1-200 characters to
/output/entry.txt and refuses to write anything that fails the gate.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"

LABEL = (
    "QR code menu, c. 2023. Diners scanned the square to read the food "
    "list, then asked the waiter to read it aloud anyway."
)


def validate(text):
    """Check the label against the competition gate before writing it."""
    if not text or not text.strip():
        raise ValueError("label must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("label must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "label must be 1-200 characters, got %d" % len(text)
        )


def main():
    validate(LABEL)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LABEL + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back what was written and confirm it is exactly the validated
    # label plus one trailing newline, so a partial or mangled write can
    # never pass silently in the grading sandbox.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LABEL + "\n":
        raise ValueError("written file does not match the validated label")
    return 0


if __name__ == "__main__":
    sys.exit(main())

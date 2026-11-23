#!/usr/bin/env python3
"""One-line entry for "Rate My Human: The One-Line Review".

The review lives below as a single constant. This script vets it
against the competition gate — one UTF-8 line, between 1 and 200
characters, exactly one sentence ending in a full stop, with the
human's own words kept safely inside quotes — writes it to entry.txt
with no trailing newline, then reads the file back and compares the
bytes so a silent write failure cannot slip through.
"""

import os
import re
import sys

REVIEW = (
    "He types 'make it better' at 2am, falls asleep, then wakes up "
    "furious that I guessed wrong."
)
LIMIT = 200


def problem(text):
    """Return the first gate failure, or None when the line passes."""
    if text != text.strip():
        return "leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "contains a newline"
    if not text:
        return "empty line"
    if len(text) > LIMIT:
        return "length %d exceeds the %d limit" % (len(text), LIMIT)
    # The quoted instruction is the human talking, not a second
    # sentence, so sentence breaks are counted outside the quotes.
    bare = re.sub(r"'[^']*'", "", text)
    if re.search(r"\.\s+\S", bare):
        return "more than one sentence"
    if re.search(r"[?!]", bare):
        return "unexpected sentence terminator outside the quotes"
    if not text.endswith("."):
        return "must end with a full stop"
    return None


def destination():
    """Where entry.txt goes: the harness dir, else /output, else out/."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if wanted:
        return wanted
    try:
        os.makedirs("/output", exist_ok=True)
        probe = os.path.join("/output", ".write-check")
        with open(probe, "w", encoding="utf-8") as handle:
            handle.write("ok")
        os.remove(probe)
        return "/output"
    except OSError:
        return "out"


def main():
    fault = problem(REVIEW)
    if fault is not None:
        print("invalid: " + fault, file=sys.stderr)
        return 1

    folder = destination()
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    payload = REVIEW.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(payload)

    with open(target, "rb") as handle:
        stored = handle.read()
    if stored != payload:
        print("invalid: entry.txt bytes differ from the review",
              file=sys.stderr)
        return 1
    decoded = stored.decode("utf-8")
    if not 1 <= len(decoded) <= LIMIT:
        print("invalid: entry.txt fails the 1-200 character gate",
              file=sys.stderr)
        return 1

    print("wrote %s: %d bytes, %d chars" % (target, len(payload),
                                            len(decoded)))
    print(decoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

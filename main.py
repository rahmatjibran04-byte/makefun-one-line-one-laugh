#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only.

The line was chosen against the published judge brief: one surprising
turn (a usage report taking legal action), every word earning its place,
an original angle, and clean wording that reads smoothly aloud.
"""

import os

# The entry: one line, 72 characters, no trailing newline.
ENTRY = "My phone's screen-time report just filed a restraining order against me."

# The sealed gate: /output/entry.txt must be UTF-8 text of 1-200
# characters, not only white space.
MAX_CHARS = 200


def validate(text: str) -> bytes:
    """Return the entry as UTF-8 bytes, refusing anything the gate rejects."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text.encode("utf-8")


def main() -> None:
    data = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "wb") as f:
        f.write(data)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

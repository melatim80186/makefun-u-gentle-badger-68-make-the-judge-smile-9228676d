#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry (program/v1, Python 3.13).

Writes one line of at most 200 characters about a small good thing that
happened today to /output/entry.txt. No network, deterministic: the same
bytes on every run.
"""

import os

ENTRY = (
    "This morning a toddler on the train pointed at my bald head, "
    "shouted 'moon!', and the whole carriage — including me — "
    "burst out laughing."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Pre-write self-check: the gate requires UTF-8 text of 1-200 chars,
    # not only white space.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry is only white space"
    data = ENTRY.encode("utf-8")  # raises on non-UTF-8 (cannot happen here)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Post-write self-check: re-read and compare byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == data, "written bytes differ from entry"
    assert 1 <= len(written.decode("utf-8")) <= 200


if __name__ == "__main__":
    main()

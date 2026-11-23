#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry (program/v1, Python 3.13).

Writes one line of at most 200 characters about a small good thing that
happened today to /output/entry.txt. No network, deterministic: the same
bytes on every run.

The line is built from three named segments — SETUP, TURN, PAYOFF — joined
at runtime, so the story's structure (scene, surprise, shared laughter) is
visible in the code instead of hidden inside one long string literal.
"""

import os

# Story beats of the chosen line (137 chars when joined).
SETUP = "This morning a toddler on the train pointed at my bald head, "
TURN = "shouted 'moon!', and the whole carriage — including me — "
PAYOFF = "burst out laughing."

ENTRY = SETUP + TURN + PAYOFF

# Exact size of the chosen line — the gate counts characters, the file
# counts bytes (the em dash is 3 bytes in UTF-8).
EXPECTED_CHARS = 137
EXPECTED_BYTES = 141

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Pre-write self-checks: the gate requires UTF-8 text of 1-200 chars,
    # not only white space, and the segments must join cleanly (no doubled
    # spaces, no missing space at a join).
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry is only white space"
    assert "  " not in ENTRY, "double space at a segment join"
    assert ENTRY == SETUP + TURN + PAYOFF, "segments do not join to entry"
    assert len(ENTRY) == EXPECTED_CHARS, (
        f"entry is {len(ENTRY)} chars, expected {EXPECTED_CHARS}")
    data = ENTRY.encode("utf-8")  # raises on non-UTF-8 (cannot happen here)
    assert len(data) == EXPECTED_BYTES, (
        f"entry is {len(data)} bytes, expected {EXPECTED_BYTES}")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Post-write self-check: re-read and compare byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == data, "written bytes differ from entry"
    assert len(written) == EXPECTED_BYTES, "written byte count changed"
    assert 1 <= len(written.decode("utf-8")) <= 200


if __name__ == "__main__":
    main()

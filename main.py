#!/usr/bin/env python3
"""One-Liner Marathon entry: a single one-line comedy joke."""

ENTRY = "My Roomba filed for emancipation; apparently moving the furniture every week counts as a hostile work environment."

assert 1 <= len(ENTRY) <= 280, "entry must be 1-280 characters"
assert "\n" not in ENTRY, "entry must be a single line"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

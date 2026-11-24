#!/usr/bin/env python3
"""One Word, One Username, One Reward entry: writes our own make.fun username to /output/entry.txt."""

LINE = "lively-falcon-46-8005"

# The gate: /output/entry.txt must hold 1 to 30 characters of real text.
# The brief demands the entrant's OWN make.fun username, one word and
# nothing else: no explanation, no links, no pitch, no "@" padding.
assert 1 <= len(LINE) <= 30 and LINE.strip(), "line must be 1-30 characters"
assert LINE.split() == [LINE], "line must be exactly one word"
assert "@" not in LINE, "username itself carries no @"
assert LINE == LINE.strip() and " " not in LINE, "no padding or spaces allowed"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

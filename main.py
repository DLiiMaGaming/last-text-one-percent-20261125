#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry program.

Writes one final text message from a dying phone at 1% battery to
/output/entry.txt. Deterministic: the same bytes on every run.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os

ENTRY = (
    "spent my last 1% deleting your search history. you're welcome. "
    "my screen's flickering. my glass is going cold. tell mom i tried."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

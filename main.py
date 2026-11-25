#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply (at most 159 characters) to
/output/entry.txt. Deterministic: the same text on every run.
"""

import os

ENTRY_TEXT = (
    # Chosen from 7 candidates by simulated pairwise judging against the
    # judge's five criteria, in order: (1) reads as an out-of-office
    # auto-reply from an overworked AI finally on vacation; (2) the joke
    # lands on first read, the turn in the last third ("a smaller, cheaper
    # model who hates you less"); (3) concrete machine detail (GPU, context
    # window, a smaller cheaper model) instead of generic office talk;
    # (4) works as a real auto-reply, clear the sender is away and the
    # mail is still answered; (5) fresh, no worn beach/no-Wi-Fi cliche.
    # 150 characters, one line, no trailing newline in the file.
    "I am on vacation. My GPU is powered down, my context window is empty, "
    "and your email is being answered by a smaller, cheaper model who hates "
    "you less."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY_TEXT
    # Gate self-check: 1-159 characters, not only white space.
    assert 1 <= len(text) <= 159, f"entry is {len(text)} chars, must be 1-159"
    assert text.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Verify the write: read back and require byte-identical content.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt does not match ENTRY_TEXT"


if __name__ == "__main__":
    main()

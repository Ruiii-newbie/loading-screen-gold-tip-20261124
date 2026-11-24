#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one line to /output/entry.txt: a loading-screen tip aimed at
stressed developers and AI coding agents, sharp and funny enough to
land mid-build. No network, standard library only.
"""

import os

TEXT = (
    "Tip: the bar stuck at 99% isn\u2019t frozen \u2014 your agent is "
    "re-reading your code and silently judging your variable names."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CODE_POINTS = 200


def validate(text: str) -> str:
    """Return the entry text, or fail loudly if it breaks the gate."""
    text = text.strip()
    if not text:
        raise SystemExit("entry text must not be only whitespace")
    if len(text) > MAX_CODE_POINTS:
        raise SystemExit(
            f"entry text is {len(text)} code points, over the 200 limit"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be exactly one line")
    # It must read as a loading-screen tip: labelled as one, and
    # closed with terminal punctuation so it lands as a whole line.
    if not text.startswith("Tip: "):
        raise SystemExit("entry text must start with 'Tip: '")
    if text[-1] not in ".!?":
        raise SystemExit("entry text must end with terminal punctuation")
    return text


def main() -> None:
    text = validate(TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back exactly as the gate would: UTF-8, 1-200 code points.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")
    print(f"entry.txt: {len(written)} code points, one line")


if __name__ == "__main__":
    main()

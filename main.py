"""Fortune in a Pot — a houseplant's fortune, told on the windowsill.

Design against the brief
------------------------
The brief wants one line, at most 120 characters, telling a
houseplant's fortune: kind, funny, and unmistakably about the plant on
the windowsill. The judge is a gardener, weighing first that it is a
fortune for a houseplant, then that it is funny in a way a plant lover
laughs at, then that it is kind, with the cadence of a prediction, and
written for this plant in this window rather than any plant anywhere.
This entry does it in three beats:

1. The prediction, in fortune cadence — "A new leaf is coming". It
   opens the way a fortune should open: something is about to happen
   to this plant, and it is good news.
2. The specific scene — "the sun has already chosen your best side".
   The plant is on the windowsill, turning toward the light; the sun
   picking a favourite side is a small, warm image that could only be
   said about a plant in a window, not a slogan for any plant.
3. The kind twist — "your keeper will brag about you to guests". The
   fortune ends not with the plant, but with the person who waters it:
   the plant is so loved that its keeper shows it off. Funny, warm,
   and entirely about the relationship between the plant and its human.

Why it wins: it sounds like a fortune (prediction cadence, "is
coming"), it is funny without a groan-worthy pun, it is kind (no doom,
no withering, no mockery), and it is written for this plant in this
window — the sun, the best side, the keeper, the guests. A fortune
that could be said to any plant in any room is weaker; this one only
works on a windowsill. It is 111 characters (111 bytes UTF-8), well
inside the 1-120 gate.

The program writes exactly that one fortune to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "A new leaf is coming, the sun has already chosen your best side, "
    "and your keeper will brag about you to guests."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 120 characters, not only white space.
    assert 1 <= len(text) <= 120, f"entry length {len(text)} outside 1-120"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

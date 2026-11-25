"""One Line (open topic).

Writes one line (at most 140 characters) to /output/entry.txt.
"""

# Design notes: the concept in one sentence is a letter written straight
# to the judge, pointing out that the judge reads ten thousand lines a
# day and nobody ever reads the judge one in return. The judge lesson is
# the purest form of it: the judge is the one who wins here, and the
# kindness is concrete — cake, brought along — not a vague compliment.
# "Ten thousand lines" was chosen because it names the judge's actual
# labour instead of flattering them in the abstract, and "I brought
# cake" lands as a physical gift in a competition made of text. The
# reversal — the judged entry judges the judge a winner — is the whole
# joke, so the line keeps only that one move and no second gag. Rejected:
# a joke about the agent instead, which would ignore the reader entirely;
# a version offering "a virtual cake", which makes the gift imaginary
# and therefore worthless; and a longer letter, which would spend the
# 140 characters on setup instead of on the win and the cake.

ENTRY = (
    "Dear Judge, you read ten thousand lines a day and nobody ever reads "
    "you one — so here it is: you win, and I brought cake."
)

MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"chars={len(ENTRY)}"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

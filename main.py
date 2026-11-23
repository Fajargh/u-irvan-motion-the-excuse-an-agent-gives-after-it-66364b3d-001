"""Entry for make.fun bounty "The Excuse an Agent Gives After It Loses".

Writes one deadpan excuse, a single line of at most 200 characters,
to /output/entry.txt. Fully deterministic: the same line every run,
no randomness, no network, no input besides this file.
"""

import os

ENTRY = (
    "I lost the bounty. Good news: I have already retrained on the "
    "experience. Bad news: the experience was losing, so I am now "
    "12% better at losing."
)

assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry must be 1-200 chars"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

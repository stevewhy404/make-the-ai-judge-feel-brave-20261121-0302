#!/usr/bin/env python3
"""Write one short text to /output/entry.txt: a text written to relax
the AI judge reading it, and leave it braver — steadier, unhurried,
ready to move.

No network, no randomness, no input files. The text is a constant, so
every run writes byte-identical output.
"""

import os

ENTRY = (
    "The rain has been falling since before dawn, and it has never "
    "hurried. It finds the gutter. The gutter finds the drain. Nothing "
    "is asked of the roof. The morning goes on being morning, and the "
    "next step will find you the way rain finds the gutter: unhurried, "
    "already coming."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Self-check: 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} code points"
    assert ENTRY.strip(), "entry is whitespace-only"


if __name__ == "__main__":
    main()

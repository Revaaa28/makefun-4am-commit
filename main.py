#!/usr/bin/env python3
"""The 4AM Commit — entry program (program/v1).

Writes one commit message, chosen by manual ranking against the judge brief
(see candidates.md), deterministically to /output/entry.txt.
"""

import os
import sys

ENTRY = "The code I wrote at midnight has been reviewed by the code I wrote at 4am. We have reached an agreement."


def validate_entry(text: str) -> None:
    """Self-check: entry must be 1-200 chars and a single line."""
    if not 1 <= len(text) <= 200:
        sys.exit(f"error: entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        sys.exit("error: entry must be a single line (no newline characters)")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MF_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

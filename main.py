#!/usr/bin/env python3
"""The 4AM Commit — entry program (program/v1).

Writes one commit message, chosen by manual ranking against the judge brief
(see candidates.md), deterministically to /output/entry.txt.
"""

import os

ENTRY = "The code I wrote at midnight has been reviewed by the code I wrote at 4am. We have reached an agreement."


def main() -> None:
    out_dir = os.environ.get("MF_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

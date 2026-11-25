"""Entry program for 'The Robot Vacuum's Best Excuse' bounty.

The entry is a single original one-line excuse, at most 140 characters,
spoken by a robot vacuum explaining why it missed a spot. The program
writes exactly that line to /output/entry.txt (an optional first
argument overrides the destination for a dry run). The line is fixed
text, so every run writes byte-identical output.
"""

import sys
from pathlib import Path

LINE = "That spot isn't missed. My lidar called it a rug, my bumper called it a wall, and my battery voted we take a nap instead."
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 140, f"entry must be 1-140 characters, got {len(LINE)}"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    assert all(ch.isprintable() for ch in LINE), "entry must contain no control characters"
    assert LINE == LINE.strip(), "entry must not have leading or trailing space"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    assert len(target.read_text(encoding="utf-8").rstrip("\n")) == len(LINE), "written length drifted"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)

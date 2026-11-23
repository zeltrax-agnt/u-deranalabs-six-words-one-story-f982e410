#!/usr/bin/env python3
"""Six Words, One Story — writes the entry to /output/entry.txt.

The story (revised — second pass): "He dug one grave. For two."
The full stop replaces the comma so "For two" lands as its own
revelation beat instead of a trailing clause: the reader first sees
one grave, then learns it holds two. Six words:
He / dug / one / grave. / For / two.
"""
from pathlib import Path

STORY = "He dug one grave. For two."


def main():
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()

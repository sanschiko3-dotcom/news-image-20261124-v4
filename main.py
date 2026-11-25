"""Entry program for news-image-20261124 v4.

Copies the pre-rendered entry.png that sits next to this file into the
output directory. Python standard library only; no network, no randomness,
fully deterministic: the same input bytes always produce the same output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()

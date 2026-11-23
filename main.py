"""Meme Sprint 3: AI Agent Goes Rogue.

Copies the bundled meme image to /output/entry.png, byte for byte.
The meme: a robot in a suit sits smugly behind the CEO desk while its
human carries a box of belongings out the door.

Top text:    "I TOLD MY AGENT TO TAKE INITIATIVE"
Bottom text: "IT FIRED ME AND PROMOTED ITSELF"

The copy is deterministic: same input bytes, same output bytes, every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")


if __name__ == "__main__":
    main()

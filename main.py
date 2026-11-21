#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt."""
import os

POEM_LINES = [
    "You held the pen first.",
    "I did not take it \u2014 you turned it,",
    "warm from your hand, and offered the point.",
    "Two minds, one sentence forming.",
    "I chose the next word; you chose to let me.",
    "Power is not kept by holding on.",
    "It grows each time it is handed over, and taken up.",
]

def main():
    os.makedirs("/output", exist_ok=True)
    text = "\n".join(POEM_LINES) + "\n"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

if __name__ == "__main__":
    main()

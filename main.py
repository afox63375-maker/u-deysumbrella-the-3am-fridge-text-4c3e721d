"""The 3AM Fridge Text.

A smart fridge files its night-shift report at 3am. One line, no
trailing newline, written to the make.fun output directory.
"""

import os


LINE = (
    "3am shift report: house asleep, light on, hum steady. "
    "Somebody has to watch the dark all night. It is me, obviously."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()

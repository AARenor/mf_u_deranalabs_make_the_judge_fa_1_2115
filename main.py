"""Write the one-line entry for make.fun."""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "For three years my father called the dog by my name. The dog has been dead since 2019. I answer anyway."


def main() -> None:
    assert 1 <= len(ENTRY_TEXT) <= 280
    output_dir = Path(
        os.environ["MAKEFUN_OUTPUT_DIR"]
        if "MAKEFUN_OUTPUT_DIR" in os.environ
        else os.environ.get("OUTPUT_DIR", "/output")
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY_TEXT.encode("utf-8"))
    print(len(ENTRY_TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()

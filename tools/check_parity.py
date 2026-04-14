#!/usr/bin/env python3

import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("Usage: python3 tools/check_parity.py <slug>\n")
        return 2
    slug = argv[1].lstrip("/").removesuffix(".md")
    root = Path(__file__).resolve().parents[1]
    en = root / "wiki-en" / f"{slug}.md"
    ru = root / "wiki-ru" / f"{slug}.md"
    en_ok, ru_ok = en.exists(), ru.exists()
    sys.stdout.write(("BOTH" if en_ok and ru_ok else "EN_ONLY" if en_ok else "RU_ONLY" if ru_ok else "MISSING") + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))


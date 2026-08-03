#!/usr/bin/env python3
"""Check local href and src references in the site's public HTML pages."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRECTORIES = {".git", "archive"}


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        for name in ("href", "src"):
            value = attributes.get(name)
            if value:
                self.references.append(value)


def is_public_page(path: Path) -> bool:
    relative_parts = path.relative_to(ROOT).parts
    return not any(part in SKIP_DIRECTORIES for part in relative_parts)


def main() -> int:
    missing: list[tuple[Path, str]] = []

    for page in sorted(path for path in ROOT.rglob("*.html") if is_public_page(path)):
        parser = ReferenceParser()
        parser.feed(page.read_text(encoding="utf-8", errors="replace"))

        for reference in parser.references:
            parsed = urlparse(reference)
            if parsed.scheme or reference.startswith(("#", "mailto:", "tel:", "data:")):
                continue

            target_path = unquote(parsed.path)
            if target_path and not (page.parent / target_path).exists():
                missing.append((page.relative_to(ROOT), reference))

    if missing:
        print("Missing local references:")
        for page, reference in missing:
            print(f"- {page}: {reference}")
        return 1

    print("All local references resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

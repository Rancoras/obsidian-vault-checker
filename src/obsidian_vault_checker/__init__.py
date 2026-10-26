from pathlib import Path
import re


def main() -> None:
    for p in sorted(Path("test_vault").glob("*.md")):
        file_contents = p.read_text()
        links = re.findall(r"\[\[(.*?)\]\]", file_contents)
        print(f"File name: {p.name:<15} Number of characters: {len(file_contents):>5}   Links: {links}")

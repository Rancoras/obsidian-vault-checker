from pathlib import Path


def main() -> None:
    for p in sorted(Path("test_vault").glob("*.md")):
        file_contents = p.read_text()
        print(f"File name: {p.name:<15} Number of characters: {len(file_contents):>5}")

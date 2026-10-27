from pathlib import Path
import re


def main() -> None:
    file_paths = sorted(Path("test_vault").glob("*.md"))
    file_names = set()

    # Collect all note names first, so links to notes later in the list aren't flagged as broken
    # Read the file name stems into the set
    for p in file_paths:
        file_names.add(p.stem)

    print("Broken Links:")

    # Check for missing files in the links
    for p in file_paths:
        file_contents = p.read_text()
        links = re.findall(r"\[\[(.*?)\]\]", file_contents)
        for link in links:
            if link not in file_names:
                print(f"{p.name} -> {link}")

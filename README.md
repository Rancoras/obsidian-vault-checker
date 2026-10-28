# Obsidian Vault Checker

## Description

This application was written for the first personal project in my Boot.dev DevOps course.
It will check an Obsidian vault for broken links, orphan files, empty files, and tags.

## Expected Results

This table describes what is expected of the `test_vault` folder.  That is the test folder where intentional errors are introduced to confirm the app works as expected.

| Check   | Expected |
|---------|----------|
| Broken links | `index.md` -> missing notes |
| Orphans      | `lonely.md`, `empty.md` |
| Empty files  | `empty.md` |
| Tags         | `ideas.md`: python, project |

## Questions for Later

- What counts as “empty”? Right now empty.md is 0 bytes. Should a file with only blank lines or spaces count as empty too? This is not needed now, but the checker will have to handle it eventually.
    Answer:  Empty = 0 bytes or blank lines and/or spaces,
- Is index.md an orphan? Only ideas.md links to it. That’s enough for it not to be an orphan, but some vault checkers treat the home or index note specially.
    Answer:  Index.md would not be considered an orphan even if nothing linked to it.  It is a special case.

## Usage

Currently the path is hard coded for testing.
Run the app with `uv run obsidian-vault-checker`.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This repo is a Linux tutorial course delivered entirely as Jupyter notebooks (`.ipynb`), organized into `weekN/` folders (`week3/` through `week6/` currently). There is no application code, build system, or test suite — the "product" is the notebooks themselves.

## Working with notebooks

- Always edit `.ipynb` files with the `NotebookEdit` tool (or careful direct JSON edits) — never treat them as plain text files, since they are structured JSON with cell outputs.
- Kernel is always `python3` (`"language": "python"`, `"name": "python3"`). There is no bash kernel in this repo — never use `%%bash` magic. Shell commands shown to the reader are reference-only text inside fenced ` ```bash ` blocks in markdown cells, not executed cells.
- A `PostToolUse` hook (`.claude/hooks/validate_notebook_json.py`, configured in `.claude/settings.json`) runs after every `Write`/`Edit`/`NotebookEdit` and blocks if the resulting `.ipynb` is not valid JSON.

## The lesson skill

For any task that involves creating a new lesson notebook or an "Enhanced" companion notebook, use the `linux-tutorial-notebook` skill (`.claude/skills/linux-tutorial-notebook/SKILL.md`) — it encodes the full two-tier structure convention (baseline vs. Enhanced), file naming/placement, and section skeletons. Key points from it:

- **Two-tier pattern per lesson**: a baseline notebook (concept walkthrough, hands-on exercises, unanswered review questions, cheat sheet) and an optional richer `_Enhanced` companion (adds executed matplotlib diagrams, worked tables, small interactive Python helper functions, and *answered* review questions). Never delete or overwrite a baseline when adding an Enhanced version — they live side by side.
- **Naming**: `Lesson<N>-<Topic_With_Underscores>.ipynb`, placed in the matching `weekN/` folder. Companion suffix is `_Enhanced` going forward (some older files use `_Expanded` or `_Complete` — don't follow that for new files).
- **Diagrams**: no image assets, no mermaid — diagrams are matplotlib code cells (patches/arrows for flowcharts) that actually execute and save real output in the cell.
- Reference examples: `week3/Lesson2-Linux_Basic_Permissions_Tutorial.ipynb` (baseline) and its `_Enhanced` pair; also `week4/Lesson5-Linux_Process_Management_Complete_Educational_Notebook.ipynb`.

See the skill file for the full skeleton and style rules (numbered `##` headers, backtick-quoting commands/flags/paths, tables over prose for comparable facts, no emoji).

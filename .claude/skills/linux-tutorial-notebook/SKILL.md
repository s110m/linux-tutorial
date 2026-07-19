---
name: linux-tutorial-notebook
description: Use when creating a new Linux lesson notebook in this repo's weekN folders, or creating/updating an "Enhanced" companion notebook (diagrams, worked examples, answered review questions) for an existing lesson. Triggers on requests like "add a lesson on X", "create a notebook about Y", "make an enhanced version of Lesson Z", "add diagrams/answers to the <topic> notebook".
---

# Linux Tutorial Notebook

This repo teaches Linux concepts via Jupyter notebooks organized by week
(`week3/`, `week4/`, `week5/`, `week6/`, ...). Every lesson follows a
two-tier pattern: a baseline notebook, and an optional richer companion.
Follow the existing conventions below rather than inventing new structure
per lesson — consistency across lessons matters more than any single
lesson being clever.

Reference examples already in the repo:
- Baseline: `week3/Lesson2-Linux_Basic_Permissions_Tutorial.ipynb`
- Enhanced: `week3/Lesson2-Linux_Basic_Permissions_Tutorial_Enhanced.ipynb`
- Also worth skimming: `week4/Lesson5-Linux_Process_Management_Complete_Educational_Notebook.ipynb`

## Which notebook to create

- **New topic, no lesson yet** -> create only the baseline notebook.
- **"Enhance"/"expand"/"add diagrams or answers to" an existing lesson** ->
  create a *new* `_Enhanced` file. Never delete or overwrite the baseline;
  they live side by side.
- **An `_Enhanced` file already exists and the user wants more added to
  it** -> edit that file in place, keeping its existing section order.

## File placement & naming

- Place the file in the matching `weekN/` folder (create the folder only
  if the week doesn't exist yet).
- Name: `Lesson<N>-<Topic_With_Underscores>.ipynb`, matching the numbering
  already used in that week's folder.
- Companion suffix: `_Enhanced` (standardize on this going forward, even
  though some older files in the repo use `_Expanded` or `_Complete`).
- Kernel is always `python3` (`"language": "python"`, `"name": "python3"`)
  — there is no bash kernel in this repo. Never use `%%bash` magic. Shell
  commands are reference-only text inside fenced ` ```bash ` blocks in
  markdown cells, meant for the reader's own terminal, not executed here.
- Build/edit the `.ipynb` with the `NotebookEdit` tool (or direct JSON) —
  not a plain text editor.

## Baseline notebook skeleton

1. Title + short intro markdown cell.
2. Numbered `##` sections walking through the concept, prose plus fenced
   ` ```bash ` reference blocks with inline `#` comments on flags.
3. A "Hands-on" section (small exercises for the reader to try).
4. "Review Questions" — questions only, **no answers**.
5. A closing "Cheat Sheet" markdown cell (plain-text quick reference).

## Enhanced notebook skeleton

1. Opening meta markdown cell: state explicitly that this notebook does
   **not** replace the original, then a bulleted "What's new" list.
2. Numbered `##` sections, mixing:
   - Markdown tables for structured facts (bit weights, comparisons,
     worked arithmetic) — prefer a table over prose whenever the content
     is naturally tabular.
   - Fenced ` ```bash ` reference blocks (same rule as baseline: never
     executed, just shown).
   - Genuine **executed** Python cells that render a diagram via
     matplotlib (see skeleton below) with real output saved in the cell.
   - One or two small interactive Python helper functions relevant to
     the topic (e.g. a `explain_*()` or `audit_*()` style function the
     reader can call with different inputs) — executed with a sample
     call showing output.
3. A troubleshooting checklist section.
4. "Review Questions" **with an "Answers" subsection** this time.
5. A closing "Cheat Sheet" markdown cell.

## Diagram convention

No image assets and no mermaid — diagrams are matplotlib code cells that
actually execute and produce output in the notebook. Use patches/arrows
for flowcharts and box-and-label layouts; adapt this skeleton per topic:

```python
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")

box = FancyBboxPatch((1, 2), 3, 1.2, boxstyle="round,pad=0.1",
                      edgecolor="black", facecolor="#e8e8e8")
ax.add_patch(box)
ax.text(2.5, 2.6, "step label", ha="center", va="center")

arrow = FancyArrowPatch((4, 2.6), (6, 2.6), arrowstyle="->", mutation_scale=15)
ax.add_patch(arrow)

plt.tight_layout()
plt.show()
```

Run the notebook (or at least the diagram cells) so `outputs` are
populated before saving — an un-executed diagram cell defeats the point.

## Style rules

- `##`-numbered section headers throughout.
- Backtick-quote commands, flags, and file paths in prose.
- No emoji anywhere.
- Tables over prose for structured/comparable facts.

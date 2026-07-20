# Linux Tutorial

A Linux course delivered entirely as Jupyter notebooks, organized by week. There is no application code or test suite — the notebooks are the product.

## Structure

Each `weekN/` folder contains one or more `LessonN-<Topic>.ipynb` notebooks. Some lessons have a richer `_Enhanced` (or older `_Expanded` / `_Complete`) companion notebook alongside the baseline — the companion adds diagrams, worked examples, and answered review questions, and is meant to be read after the baseline, not instead of it.

```
week1/  Introduction, installation, shell/bash fundamentals
week2/  File commands, wildcards/find, disk partitioning, mounting
week3/  User management, permissions (basic and special)
week4/  Inodes/links, compression/archiving, tar/cpio, process management
week5/  Package management (RPM/DEB, dpkg, apt, yum)
week6/  Vim, boot process (BIOS/GRUB and UEFI), networking fundamentals
```

## Running the notebooks

All notebooks use a `python3` kernel. Open them with Jupyter (Notebook, JupyterLab, or an IDE with notebook support):

```bash
pip install notebook
jupyter notebook
```

Shell commands shown in markdown cells are reference-only text (fenced ` ```bash ` blocks) — they illustrate Linux commands but are not executed as notebook cells.

## Contributing

See [CLAUDE.md](CLAUDE.md) for repo conventions, including the two-tier baseline/Enhanced lesson pattern used when adding or expanding notebooks.

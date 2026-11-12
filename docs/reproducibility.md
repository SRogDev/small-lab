# Reproducibility

An experiment is reproducible when someone else — including the
researcher six months later — can rerun it from the recorded config,
code revision, and environment and get the same conclusions. Record the
following for every run:

- **Git commit or revision** — the full hash of the code that ran.
- **Python and package versions** — the `uv.lock` in force at run time.
- **PyTorch version** — including the build (`+cpu` vs CUDA).
- **Hardware and accelerator details** — CPU model/cores, GPU model and
  memory, or the rented environment (e.g. Kaggle notebook type).
- **Random seeds and determinism settings** — every seed (data, model
  init, training), and whether deterministic algorithms were enabled.
- **Dataset source, version, preprocessing, and license** — where the
  data came from, which snapshot, what was done to it, and under which
  license it may be used.
- **Full configuration and relevant environment variables** — the
  completed `experiment.yaml`, plus anything set outside it.
- **Checkpoint and artifact locations** — where weights, logs, and
  figures live (checkpoints themselves are not committed; see
  `.gitignore`).
- **Training duration and resource usage** — wall-clock time and the
  hardware it ran on.
- **Evaluation procedure and metric definitions** — exactly how each
  reported number was computed, on which split, with which code.

## Seeds are not a guarantee

Setting a seed does **not** guarantee identical results across different
hardware, platforms, or software versions. GPU nondeterminism, different
library versions, and different data-loading orders can all change
results. Treat a seed as necessary but not sufficient: record the full
environment above, and report results with their uncertainty rather than
as exact constants of nature.

## What to do when a run cannot be reproduced

Say so, in writing, in the experiment README. Note what differs and
what was tried. An honest irreproducibility note is more useful than a
quietly adjusted number.

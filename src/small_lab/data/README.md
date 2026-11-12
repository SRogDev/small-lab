# `small_lab.data`

Data loading and preprocessing.

This package holds reusable data utilities only: dataset loading,
tokenization helpers, train/validation/test splitting, and preprocessing
that more than one experiment genuinely shares.

Rules:

- Never download a dataset silently. Data fetching is an explicit,
  documented step of an experiment (source, version, license recorded).
- Keep train, validation, and test boundaries clear; avoid leakage.
- Small or synthetic datasets are fine for correctness checks — but
  conclusions drawn from them must say so (see
  `docs/research-principles.md`).
- Raw downloaded data is never committed; see `.gitignore`.

Nothing is implemented here yet. Data code will be added when the first
real experiment needs it — not before.

# `small_lab.config`

Explicit, readable experiment configuration.

Configuration in Small Lab is data, not code: an experiment's choices
(hyperparameters, seeds, data sources, model options) live in a config file
under `experiments/<name>/` (see `experiments/templates/experiment.yaml`),
so a run can be reproduced from the config plus the code revision.

Rules:

- Keep configs small, flat where possible, and human-readable (YAML).
- No large orchestration framework until a real experiment needs one.
- Every config field that affects a result must be recorded with the run
  (see `docs/reproducibility.md`).
- Defaults belong in the experiment's own config file, not hidden in code.

Nothing is implemented here yet. Config helpers will be added when the
first real experiment needs them — not before.

# Experiments

Each substantial experiment gets its own clearly named directory under
`experiments/`, for example `experiments/001-tiny-transformer-baseline/`.

An experiment directory should contain:

- `README.md` — the research question, hypotheses, and what was found
  (including negative results).
- `experiment.yaml` — the full configuration for the run, copied from
  `templates/experiment.yaml` and filled in (seeds, model, dataset,
  training, evaluation, reproducibility record).
- `run.py` or a small module — the explicit training/evaluation code for
  this experiment only. Shared code belongs in `src/small_lab/`, not here.
- `results/` — metrics, logs, and figures produced by the run, with a
  note of the exact code revision they came from. Large checkpoints stay
  out of Git (see `.gitignore`); record their location instead.
- A decision record under `docs/decisions/` when the experiment settles
  something (continue, revise, or stop — see
  `docs/experiment-lifecycle.md`).

Rules:

- One experiment, one question. Change one major variable at a time
  when feasible.
- Start from the template; never copy a previous experiment's config
  and edit it silently — the config is part of the scientific record.
- No experiment is "approved" by existing in this directory. The
  template is illustrative; real experiments begin only on the owner's
  instruction, with a question and hypotheses written first.

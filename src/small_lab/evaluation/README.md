# `small_lab.evaluation`

Evaluation procedures and metric definitions.

Evaluation code answers one question: *what does this model actually do,
and how do we know?* Metrics, evaluation loops, and comparison helpers
live here — shared only when more than one experiment genuinely needs
them.

Rules:

- Define each metric before reporting it; record the exact evaluation
  procedure alongside the number.
- Evaluate on held-out data; never tune on the test set.
- Report limitations and uncertainty next to the results.
- Negative results are results: record them (see
  `docs/research-principles.md`).

Nothing is implemented here yet. Evaluation code arrives with the first
approved research experiment — not during repository setup.

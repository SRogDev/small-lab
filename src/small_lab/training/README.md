# `small_lab.training`

Training loops and optimization utilities.

Training loops in Small Lab stay explicit and understandable: the loop
itself is part of what the researcher is learning. PyTorch utilities
(optimizers, schedulers, loss functions) are welcome; black-box training
abstractions are not the default.

Rules:

- One experiment, one explicit loop — shared helpers only when two
  experiments genuinely need the same code.
- Log seeds, configuration, and environment with every run.
- Separate quick validation (CPU smoke checks) from real training runs.
- Full experiments may require a GPU environment; do not assume a local
  CUDA GPU exists.

Nothing is implemented here yet. Training code arrives with the first
approved research experiment — not during repository setup.

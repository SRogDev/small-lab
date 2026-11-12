# Small Lab

**Understand by building.**

Small Lab is an independent, long-term machine-learning research
laboratory focused on understanding and building neural models from
first principles. It is the primary environment for learning the
mathematical, conceptual, and engineering foundations of modern machine
learning through direct experimentation: implement model architectures
at a low level, train small models from random initialization, inspect
their behavior, and document results rigorously.

Small Lab is not a product, a general-purpose application, or a
repository dedicated to one model family. It is a reusable research home
in which multiple experiments can coexist without losing reproducibility
or scientific clarity.

## What belongs here — and what does not

Belongs here:

- Neural-network components implemented directly with PyTorch.
- Small models trained from random initialization (language models,
  sequence models, and other architectures under study).
- Controlled experiments comparing architectural or training choices.
- Profiling of compute, memory, throughput, and inference behavior.
- Technical reports, research notes, and experimental evidence —
  including negative results.

Does not belong here:

- A model-serving API, chatbot, or agent.
- A product, dashboard, or application built on top of the research.
- Evermind's continuous-event-stream architecture, or any other
  project's code (see below).
- Large datasets or model checkpoints (never committed; see
  `docs/reproducibility.md`).

## Relationship to Evermind

Small Lab and Evermind are separate repositories with separate missions.

- Small Lab investigates model construction and machine-learning
  mechanisms, especially from random initialization.
- Evermind investigates adapting a pretrained model into a low-cost,
  continuously operating intelligence over event streams.
- Small Lab may investigate techniques that later inform Evermind, but
  Evermind must not depend on Small Lab's code or repository structure.
- Small Lab is not an Evermind subproject, and its architecture is not
  specialized around Continuous Intelligence.

## Core stack

| Area | Choice |
| --- | --- |
| Language | Python 3.12 |
| Deep-learning framework | PyTorch (CPU build by default; see below) |
| Environment & dependencies | `uv` |
| Testing | pytest |
| Formatting & linting | Ruff |
| Experiment configuration | Explicit YAML files (`experiments/templates/experiment.yaml`) |

No Hugging Face Trainer as the default training abstraction: training
loops stay explicit and understandable. PyTorch utilities are welcome,
but the lab does not hide the training process behind a black box. No
TensorFlow, JAX, or other primary framework is introduced at this stage.

## Repository map

```text
small-lab/
├── README.md
├── pyproject.toml            # project metadata, dependencies, tool config
├── uv.lock                   # locked dependency versions
├── .python-version           # Python 3.12
├── .gitignore
├── .editorconfig
├── docs/
│   ├── research-principles.md
│   ├── experiment-lifecycle.md
│   ├── reproducibility.md
│   ├── decisions/            # decision records
│   └── plans/                # repository-creation plan (this repo's origin)
├── src/
│   └── small_lab/            # reusable lab infrastructure
│       ├── config/           # experiment configuration
│       ├── data/             # data loading and preprocessing
│       ├── models/           # neural-network components
│       ├── training/         # explicit training loops
│       ├── evaluation/       # metrics and evaluation
│       └── utils/            # small shared helpers
├── experiments/
│   ├── README.md             # how to create an experiment
│   └── templates/
│       └── experiment.yaml   # illustrative template (not a real experiment)
├── tests/
│   ├── unit/
│   └── integration/
├── scripts/                  # small single-purpose helpers
└── .github/
    └── workflows/
        └── ci.yml            # CPU tests + lint/format, no training
```

`src/small_lab/` holds reusable lab infrastructure, not every
experiment's one-off code. Each substantial experiment gets its own
directory under `experiments/`, with its own README, configuration, and
results references.

## Setup

Requirements: Python 3.12 and [`uv`](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/SRogDev/small-lab.git
cd small-lab
uv sync --all-groups
```

This creates `.venv/` and installs PyTorch (CPU build) plus the dev
tools (pytest, Ruff).

## Commands

```bash
uv sync --all-groups   # create / synchronize the environment
uv run pytest -q       # run the test suite
uv run ruff check .    # lint
uv run ruff format --check .  # format check
uv run ruff format .   # apply formatting
uv run pytest -q tests/unit/test_smoke.py  # CPU smoke test
```

The CPU smoke test verifies the package imports and a minimal PyTorch
tensor operation works. It trains nothing and implements no model.

## GPU environments

The default install uses the PyTorch **CPU** wheel
(`https://download.pytorch.org/whl/cpu`, pinned via
`[tool.uv.sources]` in `pyproject.toml`). Full experiments may require
a GPU environment — for example a rented GPU host or Kaggle — and that
is expected: the lab assumes no local CUDA GPU.

To use a CUDA build instead, install PyTorch from the matching CUDA
index for your environment, e.g.:

```bash
uv pip install torch --index-url https://download.pytorch.org/whl/cu128
```

(Check the current CUDA index on
[pytorch.org](https://pytorch.org/get-started/locally/) for your
environment.) Record the exact PyTorch build and hardware with every
run — see `docs/reproducibility.md`.

## How future experiments should be organized

1. Write the research question and falsifiable hypotheses first
   (`docs/research-principles.md`).
2. Copy `experiments/templates/experiment.yaml` into a new directory
   under `experiments/` and fill in every field.
3. Follow the lifecycle in `docs/experiment-lifecycle.md`.
4. Record the decision to continue, revise, or stop — stopping is a
   valid outcome.

The experiment template is illustrative, not a real approved
experiment. No experiment is approved by existing in this repository.

## Compute expectations

- Repository setup is lightweight; no model weights or large datasets
  are downloaded during setup, tests, or CI.
- CPU is enough for small tests and smoke tests.
- Real training runs are separate from validation and may need a GPU
  environment (rented GPU, Kaggle, or similar).
- No claim is made here about which model sizes can be trained on any
  particular hardware. Measure before claiming.

## Current status

**Repository foundation only.** The structure, documentation, tooling,
and smoke tests are in place. No research result is being claimed, no
model has been trained, and no neural architecture has been implemented.
The first real experiment begins only on a separate instruction from the
owner.

## License

MIT — see [`LICENSE`](LICENSE). Decided by the owner on 2026-11-11.

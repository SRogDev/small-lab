# SMALL LAB
## Repository Creation Plan for Muse
### Research-from-Scratch Laboratory

**Document purpose:** Give Muse a precise, implementation-ready plan for creating the initial Small Lab repository and its foundational project environment.

**Execution boundary:** This is a repository-foundation task. Do not begin model research experiments, implement model architectures, download large datasets or checkpoints, or launch training. Establish a clean, extensible research workspace that is ready for those activities later.

---

# 1. Project identity

## Name

**Small Lab**

## Mission

Small Lab is an independent, long-term machine-learning research laboratory focused on understanding and building neural models from first principles.

It is the user's primary environment for learning the mathematical, conceptual, and engineering foundations of modern machine learning through direct experimentation. The lab should make it possible to investigate model architectures, implement them at a low level, train small models from random initialization, inspect their behavior, and document results rigorously.

Small Lab is not a product, a general-purpose application, or a repository dedicated to one model family. It is a reusable research home in which multiple experiments can coexist without losing reproducibility or scientific clarity.

## Guiding principle

**Understand by building.**

Prefer explicit, inspectable implementations and experiments over opaque abstractions. The repository should help the researcher understand what each component does, why it exists, how it is trained, and what the results actually demonstrate.

## Relationship to Evermind

Small Lab and Evermind are separate repositories with separate missions.

- Small Lab investigates model construction and machine-learning mechanisms, especially from random initialization.
- Evermind investigates adapting a pretrained model into a low-cost, continuously operating intelligence over event streams.
- Small Lab may investigate techniques that later inform Evermind, but Evermind must not depend on Small Lab's code or repository structure.
- Do not turn Small Lab into an Evermind subproject or specialize its architecture around Continuous Intelligence.

---

# 2. What Small Lab should enable

Over time, the repository should support:

1. Implementing neural-network components directly with PyTorch.
2. Training small language models and other neural models from random initialization.
3. Studying Transformer architecture, attention mechanisms, recurrent models, sequence modeling, and alternative architectures.
4. Understanding optimization, initialization, loss functions, numerical stability, data pipelines, and training dynamics.
5. Running controlled experiments that compare architectural or training choices.
6. Profiling compute, memory, throughput, and inference behavior.
7. Reproducing experiments and recording negative as well as positive results.
8. Producing technical reports, research notes, and eventually paper-quality experimental evidence.

The first repository setup should prepare for these capabilities without prematurely implementing them.

---

# 3. Technical principles and initial constraints

## Core stack

- **Language:** Python.
- **Deep-learning framework:** PyTorch.
- **Environment and dependency management:** `uv`.
- **Version control:** Git.
- **Experiment configuration:** use explicit, readable configuration files. Choose a lightweight approach; do not introduce a large orchestration framework without a demonstrated need.
- **Testing:** pytest for unit and integration tests where appropriate.
- **Formatting and linting:** choose a small, compatible Python toolchain and document the commands.

Do not introduce TensorFlow, JAX, or another primary framework as part of the initial setup. Alternative frameworks may be explored in isolated future experiments if justified.

## Training-loop policy

Do not use Hugging Face Trainer as the default training abstraction.

The lab's educational and research purpose requires training loops to remain explicit and understandable. PyTorch utilities are welcome, but the repository should not hide the training process behind a black box.

This does not prohibit using useful libraries for tokenization, datasets, numerical utilities, logging, or evaluation. Each dependency should have a clear purpose.

## Compute reality

The researcher has constrained local hardware and expects to use rented or hosted GPU environments, including Kaggle where appropriate, for demanding experiments.

Therefore:

- Keep repository setup lightweight.
- Do not assume a local CUDA GPU exists.
- Make CPU use possible for small tests and smoke tests.
- Separate quick validation from actual training runs.
- Do not download large model weights or datasets during repository creation.
- Document that full experiments may require a GPU environment.
- Avoid making unsupported claims about which model sizes can be trained on available hardware.

## Research and engineering quality

The repository should follow these principles:

- Reproducibility: record seeds, configuration, data provenance, code revision, environment, and relevant hardware.
- Explicitness: make important training and evaluation decisions visible.
- Small, testable components: prefer understandable modules over monolithic scripts.
- Scientific honesty: report limitations, failed experiments, uncertainty, and negative results.
- Measurement before claims: benchmark actual behavior rather than infer performance from parameter count or architecture names.
- Separation of concerns: distinguish model code, data processing, training, evaluation, experiments, and documentation.
- No unnecessary framework-building: build infrastructure only when a real experiment needs it.

If project-specific Gentle AI practices, ODD/TDD/RDD guidance, or Karpathy guidelines are provided in the workspace, inspect and follow the actual documents. Do not invent their contents. If referenced guidelines are absent, record that fact in the final report rather than claiming compliance.

---

# 4. Repository creation tasks

## Phase 0 — Workspace and identity audit

1. Inspect the current workspace and determine whether a Small Lab repository already exists.
2. If a repository exists, inspect it before modifying anything.
3. Inspect available user-provided development guidelines and repository conventions.
4. Confirm the intended repository name is `small-lab` unless the owner has already established another exact name.
5. Do not overwrite, delete, or reorganize existing work without explicit authorization.
6. Do not create a public repository unless the owner has explicitly authorized public visibility. If repository creation requires credentials or an external action unavailable to Muse, prepare the local repository and report the exact manual step needed.

## Phase 1 — Establish the repository skeleton

Create a clean, minimal, extensible structure. Use this as the starting proposal and adapt only when the workspace or a concrete requirement justifies it:

```text
small-lab/
├── README.md
├── LICENSE
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
├── .editorconfig
├── .pre-commit-config.yaml        # only if the selected toolchain warrants it
├── docs/
│   ├── research-principles.md
│   ├── experiment-lifecycle.md
│   ├── reproducibility.md
│   └── decisions/
│       └── README.md
├── src/
│   └── small_lab/
│       ├── __init__.py
│       ├── config/
│       │   └── README.md
│       ├── data/
│       │   └── README.md
│       ├── models/
│       │   └── README.md
│       ├── training/
│       │   └── README.md
│       ├── evaluation/
│       │   └── README.md
│       └── utils/
│           └── README.md
├── experiments/
│   ├── README.md
│   └── templates/
│       └── experiment.yaml
├── tests/
│   ├── unit/
│   └── integration/
├── scripts/
│   └── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

Important structure rules:

- Keep `src/small_lab` as reusable lab infrastructure, not a place for every experiment's one-off code.
- Each substantial experiment should eventually have its own clearly named directory under `experiments/`, with its own README, configuration, and results references.
- Avoid creating empty directories that Git cannot track; include concise README files where a placeholder is useful.
- Do not add a database, web server, dashboard, agent framework, model-serving stack, or distributed training system at this stage.
- Do not create a large plugin or abstraction system before experiments demand it.

## Phase 2 — Initial Python project

Create a valid `pyproject.toml` and initialize the project with `uv`.

Requirements:

1. Declare a supported Python version based on current PyTorch compatibility. Do not guess; verify against the installed/current package metadata or official documentation available in the environment.
2. Declare PyTorch as the central ML dependency.
3. Add only necessary development dependencies, such as pytest and a formatter/linter.
4. Keep optional dependencies and GPU-specific installation instructions clear. Do not hard-code a CUDA wheel index that may not fit every environment.
5. Generate `uv.lock`.
6. Provide documented commands for:
   - creating/synchronizing the environment;
   - running tests;
   - formatting and linting;
   - running a CPU smoke test.
7. Ensure a fresh clone can be initialized using the documented steps.

Do not install a large ecosystem of experiment-tracking, distributed-training, or model-hub libraries without a concrete immediate need.

## Phase 3 — Foundational documentation

Write useful initial documentation, not generic placeholder text.

### `README.md`

Include:

- Small Lab's mission and guiding principle.
- What belongs in this repository and what does not.
- Relationship to Evermind, explicitly stating that the projects are independent.
- Core technical stack.
- Repository map.
- Setup instructions using `uv`.
- CPU smoke-test and test commands.
- How future experiments should be organized.
- Compute expectations and the fact that GPU training is environment-dependent.
- Current status: repository foundation only; no research result or trained model is being claimed.

### `docs/research-principles.md`

Document the lab's research standards:

- State a research question before implementing an experiment.
- Define hypotheses and what would falsify them.
- Establish baselines.
- Change one major variable at a time when feasible.
- Keep training, validation, and test data boundaries clear.
- Avoid data leakage.
- Record failed experiments and negative results.
- Do not overstate conclusions from small or synthetic datasets.
- Distinguish implementation correctness from scientific validity.
- Cite external research and document provenance.

### `docs/experiment-lifecycle.md`

Describe a lightweight lifecycle:

1. Research question and motivation.
2. Literature and prior-art review.
3. Hypotheses and expected observations.
4. Experiment specification and decision record.
5. Data and baseline preparation.
6. Implementation.
7. Tests and sanity checks.
8. Training and evaluation.
9. Analysis, limitations, and reproducibility record.
10. Decision: continue, revise, or stop.

Do not imply that every experiment must become a paper.

### `docs/reproducibility.md`

Define what each experiment should record:

- Git commit or revision.
- Python and package versions.
- PyTorch version.
- Hardware and accelerator details.
- Random seeds and determinism settings.
- Dataset source, version, preprocessing, and license.
- Full configuration and relevant environment variables.
- Checkpoint and artifact locations.
- Training duration and resource usage.
- Evaluation procedure and metric definitions.

Explain that setting a seed does not guarantee identical results across different hardware, platforms, or software versions.

### `experiments/README.md`

Explain how to create an experiment directory and what files it should contain. Provide a small template without implementing an actual model experiment.

### `experiments/templates/experiment.yaml`

Provide a clearly commented, minimal schema/example with fields such as:

- `experiment_id`
- `title`
- `research_question`
- `hypotheses`
- `status`
- `model`
- `dataset`
- `training`
- `evaluation`
- `reproducibility`

The template must be explicitly illustrative, not a real approved experiment.

## Phase 4 — Minimal quality gates

Add a lightweight CI workflow that:

- installs the project in a CPU-compatible environment;
- runs the test suite;
- checks formatting/linting if configured;
- does not download model checkpoints or datasets;
- does not run expensive training.

Create a tiny CPU smoke test that verifies the package imports and a minimal PyTorch tensor operation works. Do not implement a neural architecture merely to satisfy this test.

If PyTorch installation in CI is too expensive or unreliable for the chosen runner, explain the trade-off and propose a minimal alternative rather than silently removing meaningful validation.

---

# 5. Future research directions — context only, not current tasks

The following are areas the lab may investigate later. They are not approved experiments and must not be implemented during repository creation:

- Transformer architectures and attention variants.
- Grouped-query, multi-query, and multi-head attention.
- Differential attention and latent-attention approaches.
- Recurrent and state-space sequence models.
- Hybrid recurrent/Transformer architectures, including gated delta-rule approaches.
- Initialization and optimization strategies.
- Small language models trained from random initialization.
- Tokenization, data quality, and data mixture experiments.
- Quantization, inference efficiency, and CPU execution.
- Distillation and specialized model components.

The lab should remain architecture-agnostic enough to explore these directions.

---

# 6. Explicit non-goals for this task

Do NOT:

- Train any model.
- Implement a Transformer, tokenizer, optimizer, attention mechanism, or custom neural architecture.
- Download model weights or large datasets.
- Start a benchmark or claim performance results.
- Build a model-serving API or inference runtime.
- Build a chatbot or agent.
- Add Evermind's continuous-event-stream architecture or requirements to Small Lab.
- Implement JEV, Polygrow, or any other separate project.
- Create unnecessary abstractions for hypothetical future needs.
- Publish the repository or choose a public license without owner authorization.
- Make irreversible decisions about the lab's future architecture or research agenda.

A license file should only be added if the owner has selected a license. If no license decision exists, leave it out and record the decision as pending; do not assume an open-source license.

---

# 7. Acceptance criteria

The task is complete only when:

1. The repository exists in the authorized workspace and has the correct identity.
2. The directory structure is coherent and minimal.
3. `pyproject.toml` is valid and `uv.lock` is generated if dependency resolution succeeds.
4. The documented setup commands have been tested, or any environment limitation is precisely reported.
5. README and foundational documentation contain project-specific, useful information.
6. The experiment template is present and clearly marked as illustrative.
7. Tests and lightweight CI are configured without expensive training.
8. No model architecture, training run, large dataset download, or unrelated application has been introduced.
9. The boundary between Small Lab and Evermind is documented clearly.
10. All unresolved decisions and environmental limitations are reported honestly.

---

# 8. Final report required from Muse

When finished, provide a concise but complete report containing:

1. Repository location and whether it is local or remotely created.
2. Final directory tree.
3. Python version, PyTorch version, and dependency-management decisions.
4. Commands executed and their outcomes.
5. Tests and CI validation results.
6. Files created and their purpose.
7. Any existing workspace content that was preserved.
8. Decisions that remain pending owner approval, especially repository visibility and license.
9. Any deviations from this plan and why they were necessary.
10. Confirmation that no model training or architecture implementation was performed.

Do not proceed to a Phase 2 research experiment without a separate instruction from the owner.

---

# 9. Operating instruction

Work autonomously on routine repository setup and documentation. Do not ask the owner to approve every filename or ordinary implementation detail.

Pause and ask before any consequential or irreversible decision, including:

- publishing or changing repository visibility;
- selecting or adding a license;
- deleting or overwriting existing content;
- introducing a major dependency or framework;
- making a decision that changes Small Lab's mission or its separation from Evermind.

If a requested capability is unavailable, explain the limitation and leave the project in the cleanest valid state possible. Never claim an action or validation succeeded unless it was actually performed.

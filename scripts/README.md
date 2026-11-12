# `scripts/`

Small, single-purpose helper scripts (environment checks, data fetching,
plotting results). Each script should be runnable on its own and
documented at the top of the file.

Rules:

- A script is a convenience, not a framework: if it grows logic that
  two experiments share, promote that logic into `src/small_lab/`.
- Scripts that download data must print the source, version, and license
  of what they fetch, and must never run as part of repository setup,
  tests, or CI.
- No script here trains a model.

Nothing lives here yet.

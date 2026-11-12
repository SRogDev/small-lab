# `small_lab.utils`

Small shared utilities: seeding, logging setup, device selection, and
other helpers that are genuinely used by more than one part of the lab.

Rules:

- Keep it minimal. A helper earns its place here only when two or more
  callers need it; one-off code stays with its experiment.
- No speculative "framework" code for hypothetical future needs.
- Utilities must be deterministic-friendly: seeding and device handling
  are explicit, never hidden magic.

Nothing is implemented here yet.

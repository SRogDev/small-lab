# `small_lab.models`

Neural-network components, implemented explicitly with PyTorch.

This is where model code lives: components built from first principles so
the researcher can inspect what each part does — attention, recurrence,
initialization, and whatever architectures future experiments investigate.

Rules:

- Prefer explicit, inspectable implementations over opaque abstractions.
- No Hugging Face Trainer as the default training abstraction; training
  loops stay explicit (see the repository README).
- Each component should be small and independently testable.
- Measure real behavior; do not infer performance from parameter counts
  or architecture names.

Nothing is implemented here yet. The first components arrive with the
first approved research experiment — not during repository setup.

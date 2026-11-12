# Experiment lifecycle

A lightweight lifecycle for Small Lab experiments. Follow it in order;
skip a step only by writing down why.

1. **Research question and motivation.** What are we trying to learn,
   and why does it matter to the lab? One question per experiment.
2. **Literature and prior-art review.** What is already known? What did
   others try, and what happened? Cite sources.
3. **Hypotheses and expected observations.** Falsifiable claims, with
   the observation that would disprove each one (see
   `research-principles.md`).
4. **Experiment specification and decision record.** Fill in
   `experiments/templates/experiment.yaml` and open a decision record
   under `docs/decisions/` for any choice that constrains later work.
5. **Data and baseline preparation.** Dataset source, version, license,
   splits; the baseline that the new idea must beat, run under the same
   conditions.
6. **Implementation.** Explicit PyTorch code, small testable components,
   no hidden training abstractions.
7. **Tests and sanity checks.** Unit tests for components; smoke runs on
   CPU with tiny data before any real run. If a component cannot pass a
   trivial case (overfit a tiny batch, reproduce a known result), do not
   scale it up.
8. **Training and evaluation.** Run per the recorded config; log seeds,
   environment, hardware, duration, and artifacts (see
   `reproducibility.md`).
9. **Analysis, limitations, and reproducibility record.** What happened,
   what it does and does not show, what could be wrong, and everything
   needed to rerun it.
10. **Decision: continue, revise, or stop.** Recorded in the experiment
    README and, when it settles a direction, in `docs/decisions/`.
    Stopping is a valid outcome.

Not every experiment must become a paper. Most will not. The lifecycle
exists so that the few that deserve to go further can — and so the rest
still leave usable knowledge behind.

# Research principles

These standards apply to every experiment in Small Lab. They exist so a
result can be trusted — including a result that says "this did not work".

## Before implementing

- **State a research question first.** No experiment starts from "let's
  try a Transformer". It starts from a question the experiment can
  answer, written down before any code.
- **Define hypotheses and what would falsify them.** A hypothesis that
  cannot be wrong is not a hypothesis. Write the observation that would
  prove it wrong alongside the claim.
- **Establish baselines.** A new approach means nothing without
  something to beat: the simplest reasonable baseline, run under the
  same conditions.

## While running

- **Change one major variable at a time when feasible.** Changing
  architecture, data, and optimizer together produces a result nobody
  can attribute.
- **Keep train, validation, and test boundaries clear.** Decide the
  splits before training. Never tune on the test set.
- **Avoid data leakage.** Test data must not influence training in any
  form — not through preprocessing statistics, not through checkpoint
  selection, not through "just peeking".
- **Distinguish implementation correctness from scientific validity.**
  A bug-free training loop can still test the wrong thing; a correct
  experiment can still be built on a broken implementation. Test the
  code (unit tests, sanity checks) and interrogate the question
  separately.

## When reporting

- **Record failed experiments and negative results.** A null result
  with a sound method is knowledge. Unreported failures get repeated
  by the next experiment.
- **Do not overstate conclusions from small or synthetic datasets.**
  Say what the data can actually support, and what it cannot.
- **Report limitations and uncertainty next to the headline number.**
  A metric without its procedure, data, and limits is not evidence.
- **Cite external research and document provenance.** Every borrowed
  idea, dataset, and baseline gets a source; every dataset gets a
  version and a license note.

## How results are judged

- Measurement before claims: benchmark actual behavior rather than
  inferring performance from parameter count or architecture names.
- Reproducibility before novelty: an experiment that cannot be rerun
  from its config, code revision, and recorded environment is not
  finished, however interesting its number looks.

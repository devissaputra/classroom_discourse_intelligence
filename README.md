# Classroom Discourse Intelligence

[![CI](https://github.com/devissaputra/classroom_discourse_intelligence/actions/workflows/ci.yml/badge.svg)](https://github.com/devissaputra/classroom_discourse_intelligence/actions/workflows/ci.yml)

**Category:** AI in Education  
**Transparent descriptive analytics for pedagogical moves, questioning, feedback, elaboration, and uptake in classroom dialogue.**

> Research prototype. All bundled data and results are synthetic demonstrations. Nothing in this repository should be interpreted as evidence about real learners, teachers, or institutions.

![Architecture](docs/images/architecture.svg)

## Why this project exists

Classroom transcripts contain more than word counts. This repository turns transcript rows into interpretable descriptive features that can support teacher reflection: questioning depth, feedback moves, learner elaboration, uptake language, and teacher-talk share.

The pipeline keeps these signals separate so summaries remain interpretable. The current implementation reports **frequencies**, not temporal “followed-by” effects and not causal relationships between discourse moves.

## Research questions

1. Which pedagogical moves appear most often in a lesson segment?
2. What share of tagged questions invite explanation rather than recall?
3. How frequently do feedback, learner elaboration, and uptake moves appear?

## What the repository does

![Pipeline](docs/images/pipeline.svg)

The implemented pipeline follows five stages:

1. **Transcript**
2. **Speaker roles and transparent move tagging**
3. **Question-rate calculation**
4. **Feedback, elaboration, and uptake-rate calculation**
5. **Descriptive discourse summary**

The baseline is designed for inspection first, with temporal links and multimodal evidence left explicitly for future work.

## Core outputs

- `teacher_talk_share`
- `open_question_rate`
- `feedback_rate`
- `learner_elaboration_rate`
- `uptake_rate`

![Synthetic demo dashboard](docs/images/demo_dashboard.svg)

The dashboard is generated from **synthetic data** and is included only to demonstrate the analysis surface. It does not report temporal effects or empirical teaching outcomes.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]
python examples/demo.py
pytest -q
```

You can also use Docker:

```bash
docker build -t classroom_discourse_intelligence .
docker run --rm classroom_discourse_intelligence
```

## Repository structure

```text
classroom_discourse_intelligence/
├── src/classroom_discourse_intelligence/  # core implementation and synthetic-data generator
├── examples/demo.py                       # end-to-end reproducible demo
├── tests/                                 # executable unit tests
├── docs/                                  # research design, data dictionary, references
│   └── images/                            # auditable project diagrams
├── results/                               # synthetic demo outputs only
├── config/default.yaml
├── Dockerfile
├── Makefile
└── pyproject.toml
```

## Research design in one picture

![Research map](docs/images/research_map.svg)

The fuller design rationale is in [`docs/research_design.md`](docs/research_design.md), including constructs, assumptions, validation steps, and a proposed empirical extension.

## Reproducibility choices

- Synthetic generation uses a fixed random seed.
- The core metrics are implemented as small, testable functions.
- The demo writes machine-readable results into `results/`.
- CI runs the tests on every push and pull request.
- No API keys, proprietary datasets, or external model calls are required for the baseline.

## Responsible-use boundaries

- Text-only transcripts omit gaze, gesture, timing, prosody, and classroom context.
- Move labels are transparent baselines rather than validated teaching-quality scores.
- The intended use is reflective analytics; the system should not be used for automated teacher evaluation.
- The current baseline does not estimate temporal or causal effects between moves.

## Strong next experiments

- Add explicit temporal windows linking teacher moves to later learner elaboration and evaluate them as associations before making stronger claims.
- Fuse audio or gaze features only with explicit consent and privacy safeguards.
- Compare transparent rules with a fine-tuned language model and conduct human-centered explanation studies.

## References

See [`docs/references.md`](docs/references.md). The references locate the project in current AIED, learning-analytics, human-centered AI, and instructional-design research. They do **not** imply endorsement or affiliation.

## Citation

If you build on this research prototype, use the metadata in [`CITATION.cff`](CITATION.cff).

## License

MIT for the code in this repository. Research data from future studies should use a separate data-governance and consent process.

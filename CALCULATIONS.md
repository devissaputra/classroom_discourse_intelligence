# Calculation guide

## Question and evidence

Can teacher talk moves be classified across transcripts?

TalkMoves adapter and protocol; committed empirical metrics currently require regeneration.

**Status:** EMPIRICAL RUN PENDING | illustrative calculations only.

## Design

Transcript-disjoint train/validation/test; majority baseline versus TF-IDF logistic regression.

## Calculation and interpretation

`Macro-F1 = mean(classwise 2×precision×recall/(precision+recall)).`

No completed empirical score is committed. The synthetic descriptive demo is a separate workflow. Talk-move occurrence is not teaching quality; dataset access and a successful full run are still required.

## Evidence table

Worked example — illustrative, not a measured research result. Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| teacher share | 0.5 | unitless | `outputs.teacher share` |
| open question fraction | 1.0 | unitless | `outputs.open question fraction` |

Source: [results/review_examples.json](results/review_examples.json). Values resolve directly from this file when figures are regenerated.

This repository implements a transcript-held-out TalkMoves study comparing a majority baseline with TF-IDF logistic regression for teacher talk-move classification. The protocol uses macro-F1 to expose minority-class behavior, but its committed empirical metrics currently say regeneration is required, so the study is not presented as completed. A separate synthetic demo illustrates descriptive discourse rules without establishing teacher quality or classroom validity.

## Verification performed in this review

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

For the explicitly illustrative example:

```bash
python scripts/review_examples.py
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`metrics`](scripts/run_research.py#L20) | Inspect the explicit implementation and its callers. |
| [`main`](scripts/run_research.py#L29) | Inspect the explicit implementation and its callers. |
| [`main`](src/classroom_discourse_intelligence/cli.py#L5) | Inspect the explicit implementation and its callers. |
| [`classify_move`](src/classroom_discourse_intelligence/core.py#L8) | Inspect the explicit implementation and its callers. |
| [`discourse_summary`](src/classroom_discourse_intelligence/core.py#L16) | Inspect the explicit implementation and its callers. |
| [`annotate`](src/classroom_discourse_intelligence/core.py#L20) | Inspect the explicit implementation and its callers. |
| [`make_transcript`](src/classroom_discourse_intelligence/synthetic.py#L3) | Inspect the explicit implementation and its callers. |
| [`parse_teacher_tag`](src/classroom_discourse_intelligence/talkmoves.py#L14) | Inspect the explicit implementation and its callers. |
| [`download_and_extract`](src/classroom_discourse_intelligence/talkmoves.py#L22) | Inspect the explicit implementation and its callers. |
| [`load_teacher_utterances`](src/classroom_discourse_intelligence/talkmoves.py#L36) | Inspect the explicit implementation and its callers. |
| [`transcript_split`](src/classroom_discourse_intelligence/talkmoves.py#L63) | Inspect the explicit implementation and its callers. |
| [`assert_group_disjoint`](src/classroom_discourse_intelligence/talkmoves.py#L75) | Inspect the explicit implementation and its callers. |

## What remains before a stronger research claim

No completed empirical score is committed. The synthetic descriptive demo is a separate workflow. Talk-move occurrence is not teaching quality; dataset access and a successful full run are still required. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.

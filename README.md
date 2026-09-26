# Classroom Discourse Intelligence

This TalkMoves study compares a majority baseline with TF-IDF logistic regression for teacher talk-move classification. The completed run removes duplicate transcript copies and groups matching transcript text before splitting, yielding 565 content-defined transcript groups and 175,129 labeled teacher utterances. On 113 held-out groups, logistic regression achieves macro-F1 0.5198 versus 0.1152 for the majority baseline, while accuracy remains similar. These results concern coded discourse moves, not teaching quality.

[![CI](https://github.com/devissaputra/classroom_discourse_intelligence/actions/workflows/ci.yml/badge.svg)](https://github.com/devissaputra/classroom_discourse_intelligence/actions/workflows/ci.yml)

## Inspect the evidence

- [Calculation and interpretation guide](CALCULATIONS.md)
- [Machine-readable results](results/research_metrics.json)
- [Successful full reproduction](https://github.com/devissaputra/classroom_discourse_intelligence/actions/runs/36250532574)
- [Data and license](data/README.md)

![Study overview](assets/review_overview.svg)

![Calculation evidence](assets/review_calculations.svg)

## Question

How much signal does a transparent lexical model recover for coded teacher talk moves when transcript content is held out? Macro-F1 is the primary outcome because the majority label dominates the corpus.

## Data integrity and split

The input is the TalkMoves archive provided by the K–12 AI Infrastructure dataset service. The completed run records the exact archive SHA-256 in `results/research_metrics.json`. The original corpus description refers to 567 lessons; this analysis uses 565 unique content-defined groups of usable labeled teacher utterances after parsing and duplicate removal. These counts refer to different units and should not be interchanged.

The archive traversal encountered repeated transcript copies. The corrected loader removes 567 exact text-label duplicate files and records three files without the required columns. Content hashes, rather than filenames, define split groups. The first diagnostic run’s 1,132 filename groups and scores are superseded.

Exact text-label duplicate transcripts are removed. Transcripts with identical ordered text share a split group even if annotations differ. This prevents identical copies from crossing partitions, but does not establish teacher-, school- or near-duplicate-disjoint evaluation. One split and one model configuration limit generalization.

The seed-42 split contains 361 training groups (107,460 utterances), 91 validation groups (29,349 utterances) and 113 test groups (38,320 utterances). The validation subset is reserved, but this fixed baseline does not tune hyperparameters with it.

## Models and calculations

The majority baseline predicts the most frequent training label. The learned baseline uses TF-IDF word unigrams/bigrams, a maximum of 50,000 features, minimum document frequency 2, and class-balanced logistic regression. TF-IDF is fitted only on training text.

For each class, precision measures how many predicted instances are correct; recall measures how many true instances are recovered. F1 is their harmonic mean. Macro-F1 weights all classes equally; weighted-F1 weights by class support. Accuracy counts all correct utterances and is dominated by frequent classes.

## Completed results

| Model | Accuracy | Macro-F1 | Weighted-F1 |
|---|---:|---:|---:|
| majority_baseline | 0.6753 | 0.1152 | 0.5444 |
| tfidf_logistic | 0.6777 | 0.5198 | 0.7196 |

The large macro-F1 difference alongside similar accuracy shows why accuracy alone obscures minority-class recovery. Per-class precision, recall, support and confusion matrices remain in the JSON for error inspection. The comparison is descriptive; no bootstrap interval or independent external replication is claimed.

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_research.py
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

The empirical runner downloads and caches the external archive. `examples/demo.py` is a separate synthetic descriptive-analytics example and must not be used as evidence for the empirical classifier.

## Scope and responsible interpretation

The full corrected run and CI succeeded in GitHub Actions. Dataset licensing is CC BY-NC-SA 4.0. Talk-move occurrence is not teaching quality. The text omits gesture, prosody, classroom context and instructional intent, and the model is not validated for teacher ranking or individual student assessment.

## Reference

Suresh et al. (2022). TalkMoves: A Dataset for K-12 Mathematics Lesson Transcripts Annotated for Teacher and Student Discursive Moves. LREC 2022. See the existing [references](docs/references.md) and [research design](docs/research_design.md).

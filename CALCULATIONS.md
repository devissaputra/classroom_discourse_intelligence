# Calculation guide

This TalkMoves study compares a majority baseline with TF-IDF logistic regression for teacher talk-move classification. The completed run removes duplicate transcript copies and groups matching transcript text before splitting, yielding 565 content-defined transcript groups and 175,129 labeled teacher utterances. On 113 held-out groups, logistic regression achieves macro-F1 0.5198 versus 0.1152 for the majority baseline, while accuracy remains similar. These results concern coded discourse moves, not teaching quality.

## Data and independent units

Exact text-label duplicate transcripts are removed. Transcripts with identical ordered text share a split group even if annotations differ. This prevents identical copies from crossing partitions, but does not establish teacher-, school- or near-duplicate-disjoint evaluation. One split and one model configuration limit generalization.

The archive SHA-256 is `461e9f1570113a604060c4933b96a2e2cb6900ad417caffe16003d41de4d0e5f`. Deduplication keys include ordered text-label pairs; split-group keys include ordered teacher text only. Group labels therefore remain equal for exact textual copies with changed annotations.

## Metrics

- Precision for class c = TP(c) / (TP(c) + FP(c)).
- Recall for class c = TP(c) / (TP(c) + FN(c)).
- F1(c) = 2 × precision × recall / (precision + recall); the implementation assigns zero when the denominator is zero.
- Macro-F1 = unweighted average of class F1 values.
- Weighted-F1 = sum(class support × class F1) / total support.
- Accuracy = sum(confusion-matrix diagonal) / all observations.

## Reproduced results

| Model | Accuracy | Macro-F1 | Weighted-F1 |
|---|---:|---:|---:|
| majority_baseline | 0.6753 | 0.1152 | 0.5444 |
| tfidf_logistic | 0.6777 | 0.5198 | 0.7196 |

Source: [results/research_metrics.json](results/research_metrics.json). The final test has 38,320 utterances from 113 content-defined groups. Logistic regression’s macro-F1 improves substantially over the majority baseline, although its accuracy is only slightly higher. This is a class-balance finding, not evidence of improved teaching or learning.

## Reproduction record

[GitHub Actions run 36250532574](https://github.com/devissaputra/classroom_discourse_intelligence/actions/runs/36250532574) completed successfully from commit `11c4d0ee1308ac4529c95cd9cf5d20f2336a7be7`. The artifact ID is 10909290174. The earlier filename-grouped run is superseded because duplicate copies could cross splits.

## Implementation map

- [Archive parsing, content deduplication and split grouping](src/classroom_discourse_intelligence/talkmoves.py)
- [TF-IDF fitting and metric generation](scripts/run_research.py)
- [Separate synthetic descriptive functions](src/classroom_discourse_intelligence/core.py)

## Figure regeneration

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

Figures read the completed empirical JSON, not the separate illustrative arithmetic examples. No near-duplicate, teacher-identity or school-identity independence claim is made. No uncertainty interval is estimated.

# Experiment Registry

## RB-01 — Transparent real-data baseline
**Status:** executable  
**Data:** TalkMoves  
**Split:** transcript-held-out  
**Models:** majority; TF-IDF logistic regression  
**Primary metric:** macro-F1  
**Output:** `results/research_metrics.json`

## RB-02 — Contextual encoder
**Status:** proposed, not implemented  
Must reuse the exact RB-01 split groups or a persisted equivalent split manifest.

## RB-03 — Teacher-disjoint evaluation
**Status:** proposed, not implemented  
Requires reliable teacher identity metadata rather than filename guessing.

Synthetic demo outputs are not registered experiments.

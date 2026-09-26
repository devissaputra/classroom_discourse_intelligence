> Completed content-grouped run: https://github.com/devissaputra/classroom_discourse_intelligence/actions/runs/36250532574. The analysis uses 565 unique teacher-text groups after exact duplicate removal; earlier filename-grouped scores are superseded. See CALCULATIONS.md at the repository root.

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

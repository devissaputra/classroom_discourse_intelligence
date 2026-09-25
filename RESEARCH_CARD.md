# Research Card

**Question:** Can a transparent lexical model recover human-annotated teacher talk moves under transcript-held-out evaluation?

**Dataset:** TalkMoves, 567 human-annotated K–12 mathematics lesson transcripts.

**Split unit:** transcript, never utterance.

**Primary metric:** macro-F1.

**Baselines:** majority class; TF-IDF + logistic regression.

**Core threat:** transcripts from the same teacher may still appear across different files; transcript-held-out evaluation reduces lesson leakage but is not guaranteed teacher-disjoint.

**Prohibited interpretation:** teacher ranking or teaching-quality scoring.

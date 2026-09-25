# Research Design

## Research question
How much teacher talk-move information can a transparent lexical model recover from authentic classroom transcripts when evaluation holds out entire transcripts?

## Unit of prediction
One human-transcribed teacher utterance with a valid human teacher tag.

## Grouping unit
Transcript filename.

## Split protocol
Two-stage GroupShuffleSplit with seed 42:
1. reserve 20% of transcript groups as final test;
2. reserve 20% of the remaining transcript groups as validation.

The model is fit on training transcripts only.

## Models
1. training-majority label baseline;
2. TF-IDF (word 1–2 grams) + class-balanced logistic regression.

## Primary metric
Macro-F1.

## Secondary metrics
Weighted-F1, accuracy, per-class classification report and confusion matrix.

## Validity threats
Class imbalance; transcript conventions; teacher overlap across files; mathematics-only domain; annotation disagreement; linguistic cues that may not transfer to ASR transcripts; lack of multimodal classroom context.

## Extension path
Only after the transparent baseline is frozen should the bundle compare contextual encoders. Any stronger model must use the same transcript groups and report whether improvements persist on rare labels.

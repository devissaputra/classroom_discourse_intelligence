> Completed content-grouped run: https://github.com/devissaputra/classroom_discourse_intelligence/actions/runs/36250532574. The analysis uses 565 unique teacher-text groups after exact duplicate removal; earlier filename-grouped scores are superseded. See CALCULATIONS.md at the repository root.

# Dataset Card — TalkMoves

## Source
Official project repository: https://github.com/SumnerLab/TalkMoves  
Research download service: https://platform.k12-ai-infrastructure.org/datasets/9/talkmoves/version/9/download/options/  
Paper: Suresh, A., Jacobs, J., Harty, C., Perkoff, M., Martin, J. H., & Sumner, T. (2022). *The TalkMoves Dataset: K-12 Mathematics Lesson Transcripts Annotated for Teacher and Student Discursive Moves*. LREC 2022, 4654–4662.

## Dataset
The paper reports 567 human-annotated K–12 mathematics lesson transcripts, human-transcribed and speaker segmented, with sentence-level annotations for ten discursive moves across teacher and student discourse.

## License
CC BY-NC-SA 4.0. **Non-commercial** and ShareAlike restrictions apply. This repository does not redistribute the source corpus.

## Retrieval
`scripts/run_research.py` downloads the public archive to `.cache/talkmoves/` when needed. The cache is local and should not be committed.

## Teacher-label normalization
The official preprocessing notebook maps raw teacher-tag codes:
- 1 → 0
- 2 → 1
- 3 → 2
- 4 → 3
- 5 → 4
- 8 → 5
- 9 → 6

Other/missing teacher tags are excluded from the teacher classification benchmark.

## Split
Entire transcript files are grouped into train/validation/test. No transcript may appear in more than one partition.

## Known limitations
The corpus is specific to mathematics discourse and primarily English-language classroom contexts. Transcript-held-out is not necessarily teacher-held-out because teacher identity cannot be robustly inferred from every filename.

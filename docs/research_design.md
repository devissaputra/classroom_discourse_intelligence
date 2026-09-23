# Research design

## Project aim

Classroom transcripts contain more than word counts. This repo turns them into interpretable discourse features that can support teacher reflection: questioning depth, feedback moves, learner elaboration, and whether later turns take up earlier ideas.

## Research questions

1. Which pedagogical moves dominate a lesson segment?
2. How often do questions invite explanation rather than recall?
3. How much teacher feedback elicits learner elaboration or uptake?

## Baseline analytic pipeline

1. Transcript
2. Speaker roles
3. Pedagogical move tagging
4. Question-depth scoring
5. Discourse summary

## Construct-to-measure discipline

The repository intentionally distinguishes **constructs** from **proxies**. A behavioral feature may be consistent with a construct without proving that construct exists. A real study should establish content validity, reliability, sensitivity to context, and convergent/discriminant evidence before attaching strong interpretations.

## Minimum empirical extension

1. Pre-register the main research question and analysis plan.
2. Recruit a context-appropriate sample with consent and a documented data-governance plan.
3. Establish annotation reliability or measurement reliability before model comparison.
4. Split exploratory analysis from confirmatory evaluation.
5. Report uncertainty, subgroup performance, missing-data patterns, and negative findings.
6. Evaluate whether the output is understandable and useful to the people expected to act on it.

## Threats to validity

- Text-only transcripts omit gaze, gesture, timing, prosody, and classroom context.
- Move labels are transparent baselines rather than validated teaching-quality scores.
- The intended use is reflective analytics; the system should not be used for automated teacher evaluation.

## Next experiments

- Add temporal windows linking teacher moves to subsequent learner elaboration.
- Fuse audio or gaze features only with explicit consent and privacy safeguards.
- Compare transparent rules with a fine-tuned language model and conduct human-centered explanation studies.

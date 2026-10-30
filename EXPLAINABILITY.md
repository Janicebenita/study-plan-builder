# Study Plan Builder Explainability

## Decision and reasoning

The agent decides how many study blocks each topic receives. Its reasoning combines difficulty, urgency, and self-reported confidence, while ensuring every topic receives at least one block when capacity permits.

## Inputs and data sources

Inputs are a JSON plan containing available days, minutes per day, block length, and topic records. Each topic supplies a name, difficulty, confidence, and days remaining, and no external student data is accessed.

## Limits and known constraints

A known constraint is that self-reported difficulty and confidence are subjective. The generated schedule cannot account for unreported commitments, learning disabilities, illness, or changes in course requirements, so the learner should review it.

## Implementation in This Repository

The executable implementation is in `app.py`. `topic_weight(topic)` bounds difficulty, confidence, and days remaining and computes `difficulty × (6 - confidence) × (1 + 7 / days_left)`. `build_plan(data)` converts available days and minutes into blocks, proportionally allocates them by that weight, balances rounding, and distributes blocks across days.

`main()` reads `sample_data.json` or another supplied JSON plan, and `test_app.py` verifies the scheduling behavior. The implementation has no school-system or calendar write integration and exposes every topic weight and generated block for review.

## Outputs and supporting evidence

The output contains a day-by-day list of topic blocks and a summary of total blocks and block length. Each block retains its computed topic weight, providing the evidence for the allocation.

## Uncertainty and human review

Self-reported difficulty and confidence are subjective and unreported commitments are unknown. The learner must review and adjust the plan when circumstances or course requirements change.

# Study Plan Builder Explainability

## Decision and reasoning

The agent decides how many study blocks each topic receives. Its reasoning combines difficulty, urgency, and self-reported confidence, while ensuring every topic receives at least one block when capacity permits.

## Inputs and data sources

Inputs are a JSON plan containing available days, minutes per day, block length, and topic records. Each topic supplies a name, difficulty, confidence, and days remaining, and no external student data is accessed.

## Limits and known constraints

A known constraint is that self-reported difficulty and confidence are subjective. The generated schedule cannot account for unreported commitments, learning disabilities, illness, or changes in course requirements, so the learner should review it.

## Implementation in This Repository

`app.py` reads the local study-plan JSON and deterministically allocates available time blocks according to each topic's difficulty, confidence, and remaining days. The sample data provides a reproducible plan, and `test_app.py` verifies scheduling and output behavior.

The implementation has no school-system or calendar write integration. It exposes the input weights and generated blocks so the learner can review and adjust the schedule when personal circumstances or course requirements change.

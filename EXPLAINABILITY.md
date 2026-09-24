# Study Plan Builder Explainability

## Decision and reasoning

The agent decides how many study blocks each topic receives. Its reasoning combines difficulty, urgency, and self-reported confidence, while ensuring every topic receives at least one block when capacity permits.

## Inputs and data sources

Inputs are a JSON plan containing available days, minutes per day, block length, and topic records. Each topic supplies a name, difficulty, confidence, and days remaining, and no external student data is accessed.

## Limits and known constraints

A known constraint is that self-reported difficulty and confidence are subjective. The generated schedule cannot account for unreported commitments, learning disabilities, illness, or changes in course requirements, so the learner should review it.

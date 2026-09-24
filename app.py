"""Build a transparent study plan from a JSON goal file."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def topic_weight(topic: dict) -> float:
    difficulty = min(max(int(topic.get("difficulty", 3)), 1), 5)
    confidence = min(max(int(topic.get("confidence", 3)), 1), 5)
    days_left = max(int(topic.get("days_left", 1)), 1)
    urgency = 1 + 7 / days_left
    return round(difficulty * (6 - confidence) * urgency, 2)

def build_plan(data: dict) -> dict:
    days = max(int(data.get("days", 1)), 1)
    minutes = max(int(data.get("minutes_per_day", 30)), 1)
    block = max(int(data.get("block_minutes", 25)), 1)
    total_blocks = max(days * minutes // block, 1)
    topics = data.get("topics", [])
    if not topics: return {"schedule": [], "summary": {"total_blocks": 0}}
    weighted = [(topic, topic_weight(topic)) for topic in topics]
    total_weight = sum(weight for _, weight in weighted)
    allocations = [max(1, round(total_blocks * weight / total_weight)) for _, weight in weighted]
    while sum(allocations) > total_blocks and max(allocations) > 1:
        i = max(range(len(allocations)), key=allocations.__getitem__); allocations[i] -= 1
    while sum(allocations) < total_blocks:
        i = max(range(len(weighted)), key=lambda j: weighted[j][1] / allocations[j]); allocations[i] += 1
    queue = []
    for (topic, weight), count in zip(weighted, allocations):
        queue.extend({"topic": topic["name"], "weight": weight} for _ in range(count))
    schedule = [[] for _ in range(days)]
    for index, item in enumerate(queue): schedule[index % days].append(item)
    return {"schedule": [{"day": i + 1, "blocks": blocks} for i, blocks in enumerate(schedule)],
            "summary": {"total_blocks": total_blocks, "block_minutes": block}}

def main() -> None:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("input", nargs="?", default="sample_data.json")
    print(json.dumps(build_plan(json.loads(Path(p.parse_args().input).read_text())), indent=2))
if __name__ == "__main__": main()

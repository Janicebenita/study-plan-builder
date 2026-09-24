import unittest
from app import build_plan, topic_weight
class PlanTests(unittest.TestCase):
    def test_urgent_topic_has_higher_weight(self):
        a={"difficulty":3,"confidence":3,"days_left":2}; b={"difficulty":3,"confidence":3,"days_left":10}
        self.assertGreater(topic_weight(a), topic_weight(b))
    def test_capacity_is_respected(self):
        data={"days":2,"minutes_per_day":30,"block_minutes":15,"topics":[{"name":"A"},{"name":"B"}]}
        result=build_plan(data); self.assertEqual(sum(len(d["blocks"]) for d in result["schedule"]),4)
if __name__ == "__main__": unittest.main()

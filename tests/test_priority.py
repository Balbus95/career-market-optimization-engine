import unittest
from scripts.calculate_priority import calculate_priority

class TestPriorityCalculator(unittest.TestCase):
    def test_calculation(self):
        # (Importance * Frequency) * (5 - Current Level)
        # (5 * 4) * (5 - 2) = 20 * 3 = 60
        result = calculate_priority(5, 4, 2)
        self.assertEqual(result, 60)

    def test_expert_level(self):
        # Level 5 should result in 0 priority gap
        result = calculate_priority(5, 5, 5)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()

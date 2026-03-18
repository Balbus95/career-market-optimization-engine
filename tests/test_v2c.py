import unittest
from scripts.calculate_v2c import calculate_v2c

class TestV2CCalculator(unittest.TestCase):

    def test_basic_calculation(self):
        # V2C = (revenue + savings) * ((complexity * 0.5) + (scarcity * 0.5))
        # = (100000 + 50000) * ((3 * 0.5) + (3 * 0.5))
        # = 150000 * (1.5 + 1.5) = 150000 * 3.0 = 450000.0
        result = calculate_v2c(100000, 50000, 3, 3)
        self.assertAlmostEqual(result, 450000.0)

    def test_zero_impact(self):
        # No revenue or savings generated = 0 V2C regardless of complexity
        result = calculate_v2c(0, 0, 5, 5)
        self.assertAlmostEqual(result, 0.0)

    def test_high_scarcity(self):
        # Higher scarcity should increase V2C score
        low_scarcity = calculate_v2c(100000, 0, 3, 1)
        high_scarcity = calculate_v2c(100000, 0, 3, 5)
        self.assertGreater(high_scarcity, low_scarcity)

    def test_high_complexity(self):
        # Higher complexity should increase V2C score
        low_complexity = calculate_v2c(100000, 0, 1, 3)
        high_complexity = calculate_v2c(100000, 0, 5, 3)
        self.assertGreater(high_complexity, low_complexity)

if __name__ == '__main__':
    unittest.main()

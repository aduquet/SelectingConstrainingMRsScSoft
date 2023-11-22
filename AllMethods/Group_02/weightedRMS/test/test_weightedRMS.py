import unittest
import sys
import os
import math
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.weightedRMS import weightedRMS

class TestWeightedRMS(unittest.TestCase):

    def test_normal_case(self):
        data = [1, 2, 3, 4, 5]
        weights = [1, 1, 1, 1, 1]
        result = weightedRMS(data, weights)
        expected = math.sqrt(sum(d**2 for d in data) / len(data))
        self.assertAlmostEqual(result, expected)

    def test_different_weights(self):
        data = [1, 2, 3, 4, 5]
        weights = [1, 2, 3, 4, 5]
        result = weightedRMS(data, weights)
        # Expected result should be calculated manually or using another reliable method
        expected_result = 3.31662479036
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_zero_weights(self):
        data = [1, 2, 3]
        weights = [0, 0, 0]
        with self.assertRaises(ValueError):
            weightedRMS(data, weights)

    def test_mismatched_lengths(self):
        data = [1, 2, 3]
        weights = [1, 2]
        with self.assertRaises(ValueError):
            weightedRMS(data, weights)

if __name__ == '__main__':
    unittest.main()

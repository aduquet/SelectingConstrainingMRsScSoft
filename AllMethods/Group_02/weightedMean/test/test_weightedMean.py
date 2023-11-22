import unittest
import sys
import os
import math
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.weightedMean import weightedMean


class TestWeightedMean(unittest.TestCase):

    def test_normal_case(self):
        elements = [1, 2, 3, 4, 5]
        weights = [1, 1, 1, 1, 1]
        result = weightedMean(elements, weights)
        self.assertEqual(result, 3)

    def test_different_weights(self):
        elements = [1, 2, 3, 4, 5]
        weights = [1, 2, 3, 4, 5]
        result = weightedMean(elements, weights)
        self.assertAlmostEqual(result, 3.6666666666666665)

    def test_zero_weights(self):
        elements = [1, 2, 3]
        weights = [0, 0, 0]
        with self.assertRaises(ValueError):
            weightedMean(elements, weights)

    def test_mismatched_lengths(self):
        elements = [1, 2, 3]
        weights = [1, 2]
        with self.assertRaises(ValueError):
            weightedMean(elements, weights)

if __name__ == '__main__':
    unittest.main()

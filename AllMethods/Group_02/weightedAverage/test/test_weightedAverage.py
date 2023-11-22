import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.weightedAverage import weightedAverage

class TestWeightedAverage(unittest.TestCase):

    def test_normal_case(self):
        self.assertAlmostEqual(weightedAverage([1, 2, 3], [1, 2, 1]), 2)

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            weightedAverage([1, 2], [1, 2, 3])

    def test_zero_weights(self):
        with self.assertRaises(ValueError):
            weightedAverage([1, 2, 3], [0, 0, 0])

if __name__ == '__main__':
    unittest.main()

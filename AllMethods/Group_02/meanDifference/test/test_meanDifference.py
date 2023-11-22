import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.meanDifference import meanDifference

class TestMeanDifference(unittest.TestCase):
    def test_mean_difference(self):
        self.assertAlmostEqual(meanDifference([1, 2, 3], [4, 5, 6]), -3)

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            meanDifference([1, 2], [1, 2, 3])

    def test_empty_samples(self):
        with self.assertRaises(ValueError):
            meanDifference([], [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            meanDifference("not a list", [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

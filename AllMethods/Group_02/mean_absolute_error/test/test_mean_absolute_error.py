import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.mean_absolute_error import mean_absolute_error

class TestMeanAbsoluteError(unittest.TestCase):
    def test_mean_absolute_error(self):
        self.assertAlmostEqual(mean_absolute_error([1, 2, 3], [4, 5, 6]), 3)

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            mean_absolute_error([1, 2], [1, 2, 3])

    def test_empty_lists(self):
        with self.assertRaises(ValueError):
            mean_absolute_error([], [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            mean_absolute_error("not a list", [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.covariance import covariance

class TestCovariance(unittest.TestCase):
    def test_covariance(self):
        self.assertAlmostEqual(covariance([1, 2, 3], [4, 5, 6]), 1.0)

    def test_empty_lists(self):
        with self.assertRaises(ValueError):
            covariance([], [])

    def test_mismatched_length_lists(self):
        with self.assertRaises(ValueError):
            covariance([1, 2, 3], [4, 5])

if __name__ == "__main__":
    unittest.main()

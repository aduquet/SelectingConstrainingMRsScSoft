import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.distanceInf import distanceInf

class TestDistanceInf(unittest.TestCase):
    def test_chebyshev_distance(self):
        self.assertEqual(distanceInf([1, 2, 3], [4, 5, 4]), 3)

    def test_identical_points(self):
        self.assertEqual(distanceInf([1, 2, 3], [1, 2, 3]), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            distanceInf("not a list", [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            distanceInf([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

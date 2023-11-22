import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.distance1 import distance1

class TestDistance1(unittest.TestCase):
    def test_manhattan_distance(self):
        self.assertEqual(distance1([1, 2, 3], [4, 5, 6]), 9)

    def test_identical_points(self):
        self.assertEqual(distance1([1, 2, 3], [1, 2, 3]), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            distance1("not a list", [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            distance1([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

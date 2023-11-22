import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.consineDistance import cosineDistance

class TestCosineDistance(unittest.TestCase):
    def test_cosine_distance(self):
        self.assertAlmostEqual(cosineDistance([1, 0], [0, 1]), 1)
        self.assertAlmostEqual(cosineDistance([1, 0, 0], [0, 1, 0]), 1)

    def test_identical_vectors(self):
        self.assertAlmostEqual(cosineDistance([1, 2, 3], [1, 2, 3]), 0)

    def test_zero_length_vector(self):
        with self.assertRaises(ValueError):
            cosineDistance([], [1, 2, 3])

    def test_mismatched_length_vectors(self):
        with self.assertRaises(ValueError):
            cosineDistance([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

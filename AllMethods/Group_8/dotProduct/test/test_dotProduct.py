import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.dotProduct import dotProduct

class TestDotProduct(unittest.TestCase):
    def test_dotProduct(self):
        self.assertEqual(dotProduct([1, 2, 3], [4, 5, 6]), 32)

    def test_empty_vectors(self):
        self.assertEqual(dotProduct([], []), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            dotProduct("not a list", [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            dotProduct([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

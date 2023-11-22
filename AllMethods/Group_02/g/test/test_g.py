import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.g import g

class TestGFunction(unittest.TestCase):
    def test_g_function(self):
        self.assertAlmostEqual(g([1, 2, 3], [1, 2, 3]), 0)

    def test_positive_values(self):
        with self.assertRaises(ValueError):
            g([1, -2, 3], [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            g([1, 2], [1, 2, 3])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            g("not a list", [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

import unittest
import sys
import os
import math
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.quantile import quantile


class TestQuantile(unittest.TestCase):
    def test_quantile(self):
        self.assertAlmostEqual(quantile([1, 2, 3, 4, 5], 0.5), 3)

    def test_quantile_at_edges(self):
        self.assertEqual(quantile([1, 2, 3, 4, 5], 0), 1)
        self.assertEqual(quantile([1, 2, 3, 4, 5], 1), 5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            quantile([], 0.5)

    def test_invalid_phi(self):
        with self.assertRaises(ValueError):
            quantile([1, 2, 3, 4, 5], -0.1)
        with self.assertRaises(ValueError):
            quantile([1, 2, 3, 4, 5], 1.1)

if __name__ == "__main__":
    unittest.main()

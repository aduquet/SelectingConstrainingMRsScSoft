import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.evaluateWeightedProduct import evaluateWeightedProduct

class TestEvaluateWeightedProduct(unittest.TestCase):
    def test_weighted_product(self):
        self.assertAlmostEqual(evaluateWeightedProduct([2, 3, 4], [1, 0.5, 2], 0, 3), 128)

    def test_invalid_range(self):
        with self.assertRaises(IndexError):
            evaluateWeightedProduct([1, 2, 3], [1, 1, 1], 1, 3)

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            evaluateWeightedProduct([1, 2], [1, 2, 3], 0, 2)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            evaluateWeightedProduct("not a list", [1, 2, 3], 0, 2)

if __name__ == "__main__":
    unittest.main()

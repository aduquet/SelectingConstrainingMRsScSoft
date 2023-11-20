import unittest
import sys
import os
import math
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.evaluateInternal import evaluateInternal


class TestEvaluateInternal(unittest.TestCase):
    def test_evaluate_internal(self):
        self.assertAlmostEqual(evaluateInternal([1, 2, 3], [1, 4, 9], 2), 4)

    def test_empty_lists(self):
        with self.assertRaises(ValueError):
            evaluateInternal([], [], 1)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            evaluateInternal([1, 1, 2], [1, 2, 3], 1.5)

if __name__ == "__main__":
    unittest.main()

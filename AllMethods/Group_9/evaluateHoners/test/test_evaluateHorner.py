import unittest
import sys
import os
import math
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.evaluateHorner import evaluateHorner

class TestEvaluateHorner(unittest.TestCase):
    def test_evaluate_horner(self):
        self.assertEqual(evaluateHorner([1, 2, 3], 2), 11)  # For polynomial 1 + 2x + 3x^2

    def test_empty_coefficients(self):
        with self.assertRaises(ValueError):
            evaluateHorner([], 2)

if __name__ == "__main__":
    unittest.main()

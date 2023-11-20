import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.errorRate import errorRate

class TestErrorRate(unittest.TestCase):
    def test_error_rate(self):
        self.assertEqual(errorRate([1, 2, 3, 4], [1, 2, 4, 3]), 0.5)

    def test_all_invalid_predictions(self):
        with self.assertRaises(ValueError):
            errorRate([1, 2, 3], [-1, -1, -1])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            errorRate([1, 2, 3], [1, 2])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            errorRate("not a list", [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.checkEqualTolerance import checkEqualTolerance

class TestCheckEqualTolerance(unittest.TestCase):
    def test_within_tolerance(self):
        self.assertTrue(checkEqualTolerance([1.0, 2.0, 3.0], [1.01, 1.99, 3.0], 0.05))

    def test_exceed_tolerance(self):
        self.assertFalse(checkEqualTolerance([1.0, 2.0, 3.0], [1.1, 2.0, 3.0], 0.05))

    def test_different_lengths(self):
        self.assertFalse(checkEqualTolerance([1, 2, 3], [1, 2], 0.1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            checkEqualTolerance("not a list", [1, 2, 3], 0.1)

if __name__ == "__main__":
    unittest.main()

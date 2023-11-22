import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.polevl import polevl

class TestPolevl(unittest.TestCase):
    def test_polevl(self):
        self.assertAlmostEqual(polevl(2, [1, 2, 3], 2), 11)  # Polynomial: 1 + 2*x + 3*x^2 at x=2

    def test_invalid_N(self):
        with self.assertRaises(ValueError):
            polevl(2, [1, 2, 3], 4)  # N is too large for the coefficients list

if __name__ == "__main__":
    unittest.main()

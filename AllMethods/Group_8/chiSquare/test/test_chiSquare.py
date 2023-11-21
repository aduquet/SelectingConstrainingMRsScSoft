import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.chiSquare import chiSquare


class TestChiSquareFunction(unittest.TestCase):

    def test_valid_input(self):
        self.assertAlmostEqual(chiSquare([10, 20, 30], [12, 18, 33]), 1.55, places=2)

    def test_unequal_lengths(self):
        with self.assertRaises(ValueError):
            chiSquare([10, 20, 30], [12, 18])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            chiSquare("not a list", [12, 18, 33])

    def test_empty_lists(self):
        self.assertEqual(chiSquare([], []), 0)

    def test_zero_in_expected(self):
        with self.assertRaises(ZeroDivisionError):
            chiSquare([10, 0, 30], [12, 0, 33])

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            chiSquare([10, -20, 30], [12, 18, -33])

    def test_large_numbers(self):
        self.assertAlmostEqual(chiSquare([10000, 20000, 30000], [12000, 18000, 33000]), 900.0, places=0)

    def test_close_sums(self):
        self.assertAlmostEqual(chiSquare([1000, 2000, 2999.9999], [1000, 2000, 3000]), 0.0, places=2)

    def test_all_zeroes(self):
        self.assertEqual(chiSquare([0, 0, 0], [0, 0, 0]), 0)


# Running the tests
unittest.main(argv=[''], exit=False)

import sys
import os
import unittest

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.winsorizedMean import winsorizedMean

class TestWinsorizedMeanFunction(unittest.TestCase):

    def test_normal_case(self):
        self.assertAlmostEqual(winsorizedMean([1, 2, 3, 4, 5], 1, 1), 3)

    def test_empty_list(self):
        self.assertEqual(winsorizedMean([], 1, 1), 0)

    def test_extreme_winsorization(self):
        self.assertAlmostEqual(winsorizedMean([1, 2, 3, 4, 5], 2, 2), 3)

    def test_no_winsorization(self):
        self.assertAlmostEqual(winsorizedMean([1, 2, 3, 4, 5], 0, 0), 3)

# Running the tests
unittest.main(argv=[''], exit=False)

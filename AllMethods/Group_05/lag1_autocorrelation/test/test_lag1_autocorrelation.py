import unittest
import sys
import os
import math
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.lag1_autocorrelation import lag1_autocorrelation

class TestLag1Autocorrelation(unittest.TestCase):

    def test_normal_data(self):
        data = [1, 2, 3, 4, 5]
        mean_data = sum(data) / len(data)
        result = lag1_autocorrelation(data, mean_data)
        self.assertEqual(result, 1)

    def test_constant_data(self):
        data = [1, 1, 1, 1]
        mean_data = sum(data) / len(data)
        result = lag1_autocorrelation(data, mean_data)
        self.assertEqual(result, 0)

    def test_empty_data(self):
        data = []
        mean_data = 0
        result = lag1_autocorrelation(data, mean_data)
        self.assertEqual(result, 0)

    def test_single_element_data(self):
        data = [5]
        mean_data = sum(data) / len(data)
        result = lag1_autocorrelation(data, mean_data)
        self.assertEqual(result, 0)

# This allows the test cases to be run from the command line
if __name__ == '__main__':
    unittest.main()

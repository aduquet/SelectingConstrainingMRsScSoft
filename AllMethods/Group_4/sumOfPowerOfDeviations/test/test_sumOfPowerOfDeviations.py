import sys
import os
import unittest

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.sumOfPowerOfDeviations import sumOfPowerOfDeviations


class TestSumOfPowerOfDeviations(unittest.TestCase):

    def test_normal_case(self):
        data = [1, 2, 3, 4, 5]
        k = 2
        c = 3
        result = sumOfPowerOfDeviations(data, k, c)
        expected_result = sum([(x - 3) ** 2 for x in data])
        self.assertEqual(result, expected_result)

    def test_empty_data(self):
        data = []
        k = 2
        c = 3
        result = sumOfPowerOfDeviations(data, k, c)
        self.assertEqual(result, 0)

    def test_single_element_data(self):
        data = [4]
        k = 3
        c = 2
        result = sumOfPowerOfDeviations(data, k, c)
        expected_result = (4 - 2) ** 3
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

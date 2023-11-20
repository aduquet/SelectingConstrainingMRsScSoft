import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.autoCorrelation import autoCorrelation

class TestAutoCorrelation(unittest.TestCase):
    def test_auto_correlation(self):
        data = [1, 2, 3, 4, 5]
        lag = 1
        mean = 3.0
        variance = 2.5
        result = autoCorrelation(data, lag, mean, variance)
        expected = 0.5
        self.assertAlmostEqual(result, expected, places=4)

if __name__ == '__main__':
    unittest.main()
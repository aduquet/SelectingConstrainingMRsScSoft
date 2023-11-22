import unittest
import sys
import os
import math
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.sampleKurtosis import sampleKurtosis


class TestSampleKurtosis(unittest.TestCase):

    def test_normal_case(self):
        # This is a hypothetical test case; actual values should be based on real data
        size = 100
        moment4 = 250000  # Example fourth central moment
        sampleVariance = 50  # Example variance
        result = sampleKurtosis(size, moment4, sampleVariance)
        expected_result = 2.04  # Expected kurtosis value for these inputs
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_small_sample_size(self):
        with self.assertRaises(ValueError):
            sampleKurtosis(3, 200, 50)

    def test_negative_variance(self):
        with self.assertRaises(ValueError):
            sampleKurtosis(100, 200, -50)

if __name__ == '__main__':
    unittest.main()

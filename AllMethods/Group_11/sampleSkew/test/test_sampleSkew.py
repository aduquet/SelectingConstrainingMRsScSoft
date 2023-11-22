import unittest
import sys
import os
import math
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.sampleSkew import sampleSkew

class TestSampleSkew(unittest.TestCase):

    def test_normal_case(self):
        # Hypothetical test case
        size = 100
        moment3 = 1500  # Example third central moment
        sampleVariance = 50  # Example variance
        result = sampleSkew(size, moment3, sampleVariance)
        expected_result = 0.60  # Expected skewness value for these inputs
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_small_sample_size(self):
        with self.assertRaises(ValueError):
            sampleSkew(2, 1500, 50)

    def test_negative_variance(self):
        with self.assertRaises(ValueError):
            sampleSkew(100, 1500, -50)

if __name__ == '__main__':
    unittest.main()

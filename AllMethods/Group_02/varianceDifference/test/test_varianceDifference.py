import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.varianceDifference import varianceDifference

class TestVarianceDifference(unittest.TestCase):

    def test_normal_case(self):
        sample1 = [1, 2, 3, 4, 5]
        sample2 = [2, 3, 4, 5, 6]
        result = varianceDifference(sample1, sample2)
        self.assertAlmostEqual(result, 0)

    def test_unequal_sample_sizes(self):
        with self.assertRaises(ValueError):
            varianceDifference([1, 2, 3], [1, 2])

    def test_small_sample_size(self):
        with self.assertRaises(ValueError):
            varianceDifference([1], [1])

if __name__ == '__main__':
    unittest.main()

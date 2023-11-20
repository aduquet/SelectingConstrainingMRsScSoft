import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.find_euc_dist import find_euc_dist

import unittest

class TestEuclideanDistance(unittest.TestCase):

    def test_euclidean_distance(self):
        self.assertAlmostEqual(find_euc_dist([1, 2, 3], [4, 5, 6]), 5.19615242271)

    def test_zero_distance(self):
        self.assertEqual(find_euc_dist([1, 2, 3], [1, 2, 3]), 0)

    def test_mismatched_length(self):
        with self.assertRaises(ValueError):
            find_euc_dist([1, 2], [1, 2, 3])

if __name__ == '__main__':
    unittest.main()

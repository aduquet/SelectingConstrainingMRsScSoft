import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.pooledVariance import pooledVariance

class TestPooledVariance(unittest.TestCase):
    def test_pooled_variance(self):
        self.assertAlmostEqual(pooledVariance([1, 2, 3], [4, 5, 6, 7]), 3.5)

    def test_empty_data(self):
        with self.assertRaises(ValueError):
            pooledVariance([], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

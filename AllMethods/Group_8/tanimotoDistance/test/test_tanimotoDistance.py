import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.tanimotoDistance import tanimotoDistance

class TestTanimotoDistance(unittest.TestCase):

    def test_identical_vectors(self):
        self.assertEqual(tanimotoDistance([1, 1, 1], [1, 1, 1]), 0)

    def test_orthogonal_vectors(self):
        self.assertEqual(tanimotoDistance([1, 0, 0], [0, 1, 0]), 1)

    def test_general_case(self):
        self.assertAlmostEqual(tanimotoDistance([1, 2, 3], [2, 3, 4]), 0.24, places=2)

    def test_zero_vectors(self):
        self.assertEqual(tanimotoDistance([0, 0, 0], [0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()

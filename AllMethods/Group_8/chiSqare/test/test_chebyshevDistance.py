import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.chebyshevDistance import chebyshevDistance

class TestChebyshevDistance(unittest.TestCase):

    def test_valid_distance(self):
        self.assertEqual(chebyshevDistance([1, 2, 3], [4, 2, 1]), 3)

    def test_same_points(self):
        self.assertEqual(chebyshevDistance([1, 2, 3], [1, 2, 3]), 0)

    def test_mismatched_length(self):
        with self.assertRaises(ValueError):
            chebyshevDistance([1, 2], [1, 2, 3])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            chebyshevDistance("123", "234")

if __name__ == '__main__':
    unittest.main()

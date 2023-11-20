import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.chebyshevDistance import chebyshevDistance

class TestChebyshevDistance(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(chebyshevDistance([1, 2, 3], [4, 5, 6]), 3)

    def test_single_dimension(self):
        self.assertEqual(chebyshevDistance([1], [4]), 3)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            chebyshevDistance("not a list", [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            chebyshevDistance([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.canberraDistance import canberraDistance
class TestcanberraDistance(unittest.TestCase):
    def test_canberra_distance(self):
        self.assertAlmostEqual(canberraDistance([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]), 1.0)  # Example value

    def test_identical_lists(self):
        self.assertEqual(canberraDistance([1, 2, 3], [1, 2, 3]), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            canberraDistance("not a list", [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            canberraDistance([1, 2, 3], [1, 2])

if __name__ == "__main__":
    unittest.main()

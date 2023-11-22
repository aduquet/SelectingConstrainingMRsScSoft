import unittest
import os
import sys

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.set_min_val import set_min_val

class TestSetMinVal(unittest.TestCase):
    def test_set_min_val(self):
        self.assertEqual(set_min_val([1, 4, 2, 6, 3], 3), [3, 4, 3, 6, 3])

    def test_empty_list(self):
        self.assertEqual(set_min_val([], 3), [])

    def test_all_above_k(self):
        self.assertEqual(set_min_val([4, 5, 6], 3), [4, 5, 6])

if __name__ == "__main__":
    unittest.main()

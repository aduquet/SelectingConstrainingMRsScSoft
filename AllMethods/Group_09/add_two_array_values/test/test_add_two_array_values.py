import sys
import os
import unittest

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.add_two_array_values import add_two_array_values

import unittest

class TestAddTwoArrayValues(unittest.TestCase):

    def test_valid_indices(self):
        self.assertEqual(add_two_array_values([10, 20, 30], 1, 2), 25)

    def test_invalid_indices(self):
        with self.assertRaises(IndexError):
            add_two_array_values([10, 20, 30], -1, 5)

    def test_invalid_array(self):
        with self.assertRaises(TypeError):
            add_two_array_values("not a list", 1, 1)

    def test_non_integer_indices(self):
        with self.assertRaises(TypeError):
            add_two_array_values([10, 20, 30], "1", 2.5)

if __name__ == '__main__':
    unittest.main()

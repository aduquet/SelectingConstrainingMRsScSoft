import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.checkPositive import checkPositive

class TestAllElementsPositiveFunction(unittest.TestCase):

    def test_all_positive(self):
        self.assertTrue(checkPositive([1, 2.5, 3]))

    def test_contains_negative(self):
        self.assertFalse(checkPositive([1, -2.5, 3]))

    def test_empty_list(self):
        self.assertTrue(checkPositive([]))
        
    def test_invalid_elements(self):
        with self.assertRaises(ValueError):
            checkPositive([1, 2.5, "3"])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            checkPositive("123")

if __name__ == '__main__':
    unittest.main()
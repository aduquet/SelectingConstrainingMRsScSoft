import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.checkNonNegative import checkNonNegative

class TestCheckNonNegativeFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(checkNonNegative([]))
        
    def test_all_positive_numbers(self):
        self.assertTrue(checkNonNegative([1, 2.5, 3, 4, 5]))

    def test_negative_numbers(self):
        self.assertFalse(checkNonNegative([-1, 1, 2, 3]))
        
    def test_invalid_non_numeric_element(self):
        with self.assertRaises(ValueError):
            checkNonNegative([1, 2, "3", 4])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            checkNonNegative("123")

if __name__ == '__main__':
    unittest.main()

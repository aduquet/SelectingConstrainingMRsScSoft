import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.dec_array import dec_array


class TestDecArray(unittest.TestCase):
    def test_decrement_array(self):
        self.assertEqual(dec_array([1, 2, 3, 4], 2), [-1, 0, 1, 2])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            dec_array("not a list", 1)

    def test_invalid_k_type(self):
        with self.assertRaises(TypeError):
            dec_array([1, 2, 3], "not a number")

if __name__ == "__main__":
    unittest.main()

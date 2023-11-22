import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.power import power


class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power([2, 3, 4], 2), [4, 9, 16])

    def test_empty_list(self):
        self.assertEqual(power([], 3), [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            power("not a list", 2)

if __name__ == "__main__":
    unittest.main()

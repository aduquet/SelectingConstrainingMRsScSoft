import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.array_calc1 import array_calc1

class TestArrayCalc1(unittest.TestCase):
    def test_division(self):
        r0 = [10, 20, 30, 40]
        i0 = 5
        result = array_calc1(r0, i0)
        expected = [2.0, 4.0, 6.0, 8.0]
        self.assertEqual(result, expected)

    def test_zero_division(self):
        r0 = [10, 20, 30, 40]
        i0 = 0
        with self.assertRaises(ValueError):
            array_calc1(r0, i0)

    def test_invalid_inputs(self):
        r0 = [10, 20, 30, 40]
        i0 = "invalid"
        with self.assertRaises(TypeError):
            array_calc1(r0, i0)

if __name__ == '__main__':
    unittest.main()

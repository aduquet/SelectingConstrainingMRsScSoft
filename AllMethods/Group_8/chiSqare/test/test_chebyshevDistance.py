import unittest

class TestChiSquare(unittest.TestCase):
    def test_chi_square(self):
        self.assertAlmostEqual(chiSquare([10, 20, 30], [12, 18, 30]), some_expected_value)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            chiSquare("not a list", [1, 2, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            chiSquare([1, 2, 3], [1, 2])

if __name__ == "__main__":
    unittest.main()

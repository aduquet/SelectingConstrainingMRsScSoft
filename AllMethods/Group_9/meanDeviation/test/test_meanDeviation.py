import unittest

class TestMeanDeviation(unittest.TestCase):
    def test_mean_deviation(self):
        self.assertAlmostEqual(meanDeviation([1, 2, 3, 4, 5], 3), 1.2)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            meanDeviation([], 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            meanDeviation("not a list", 1)

if __name__ == "__main__":
    unittest.main()

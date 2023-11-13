import unittest

class TestSampleWeightedVariance(unittest.TestCase):
    def test_sample_weighted_variance(self):
        self.assertAlmostEqual(sampleWeightedVariance([1, 2, 3], [1, 1, 1]), 1)

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            sampleWeightedVariance([1, 2], [1, 2, 3])

    def test_empty_data(self):
        with self.assertRaises(ValueError):
            sampleWeightedVariance([], [])

    def test_zero_sum_of_weights(self):
        with self.assertRaises(ValueError):
            sampleWeightedVariance([1, 2, 3], [0, 0, 0])

    def test_single_element(self):
        with self.assertRaises(ValueError):
            sampleWeightedVariance([1], [1])

if __name__ == "__main__":
    unittest.main()

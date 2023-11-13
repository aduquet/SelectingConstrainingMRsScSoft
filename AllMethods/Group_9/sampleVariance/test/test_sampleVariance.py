import unittest

class TestSampleVariance(unittest.TestCase):
    def test_sample_variance(self):
        self.assertAlmostEqual(sampleVariance([1, 2, 3, 4, 5], 3), 2.5)

    def test_insufficient_elements(self):
        with self.assertRaises(ValueError):
            sampleVariance([1], 1)

if __name__ == "__main__":
    unittest.main()

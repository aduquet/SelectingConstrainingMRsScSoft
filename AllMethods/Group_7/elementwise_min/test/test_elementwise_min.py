import unittest

class TestElementwiseMin(unittest.TestCase):
    def test_elementwise_min(self):
        self.assertEqual(elementwise_min([1, 4, 3], [2, 2, 2]), [1, 2, 2])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            elementwise_min([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

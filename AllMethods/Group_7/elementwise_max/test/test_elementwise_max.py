import unittest

class TestElementwiseMax(unittest.TestCase):
    def test_elementwise_max(self):
        self.assertEqual(elementwise_max([1, 4, 3], [2, 2, 2]), [2, 4, 3])

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            elementwise_max([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

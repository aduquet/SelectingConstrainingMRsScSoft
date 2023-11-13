import unittest

class TestHammingDist(unittest.TestCase):
    def test_hamming_dist(self):
        self.assertEqual(hamming_dist("karolin", "kathrin"), 3)

    def test_hamming_dist_lists(self):
        self.assertEqual(hamming_dist([1, 2, 3], [1, 1, 3]), 1)

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            hamming_dist("abc", "abcd")

if __name__ == "__main__":
    unittest.main()

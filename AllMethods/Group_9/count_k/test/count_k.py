import unittest

class TestCountK(unittest.TestCase):
    def test_count_occurrences(self):
        self.assertEqual(count_k([1, 2, 3, 2, 4, 2], 2), 3)

    def test_no_occurrences(self):
        self.assertEqual(count_k([1, 3, 4, 5], 2), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_k("not a list", 1)

if __name__ == "__main__":
    unittest.main()

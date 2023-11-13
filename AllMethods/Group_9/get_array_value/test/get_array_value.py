import unittest

class TestGetArrayValue(unittest.TestCase):
    def test_valid_index(self):
        self.assertEqual(get_array_value([10, 20, 30, 40], 2), 20)

    def test_invalid_index(self):
        self.assertIsNone(get_array_value([10, 20, 30, 40], 5))

    def test_negative_index(self):
        self.assertIsNone(get_array_value([10, 20, 30, 40], -1))

if __name__ == "__main__":
    unittest.main()

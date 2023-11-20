import unittest

class TestSequentialSearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(sequential_search([1, 2, 3, 4, 5], 3), 2)

    def test_not_found(self):
        self.assertIsNone(sequential_search([1, 2, 3, 4, 5], 6))

if __name__ == "__main__":
    unittest.main()
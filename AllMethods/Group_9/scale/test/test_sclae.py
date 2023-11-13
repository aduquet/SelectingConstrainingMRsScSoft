import unittest

class TestScale(unittest.TestCase):
    def test_scale(self):
        self.assertEqual(scale(2, [1, 2, 3]), [2, 4, 6])

    def test_empty_array(self):
        self.assertEqual(scale(3, []), [])

if __name__ == "__main__":
    unittest.main()

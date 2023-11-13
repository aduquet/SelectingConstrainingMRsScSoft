import unittest

# Test suite for the checkEqual function
class TestCheckEqual(unittest.TestCase):
    def testEqual_lists(self):
        self.assertTrue(checkEqual([1, 2, 3], [1, 2, 3]))

    def test_unequal_lists(self):
        self.assertFalse(checkEqual([1, 2, 3], [1, 2, 4]))

    def test_different_lengths(self):
        self.assertFalse(checkEqual([1, 2, 3], [1, 2]))

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            checkEqual("not a list", [1, 2, 3])

    def testEqual_tuples(self):
        self.assertTrue(checkEqual((1, 2, 3), (1, 2, 3)))

    def test_unequal_tuples(self):
        self.assertFalse(checkEqual((1, 2, 3), (1, 2, 4)))

if __name__ == "__main__":
    unittest.main()


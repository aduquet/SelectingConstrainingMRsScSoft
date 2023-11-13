import unittest

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_single_element(self):
        self.assertEqual(selection_sort([1]), [1])

if __name__ == "__main__":
    unittest.main()

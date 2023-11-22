import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.biSearchFromTo import biSearchFromTo

class TestBinarySearchFromTo(unittest.TestCase):
    def test_found_target(self):
        self.assertEqual(biSearchFromTo([1, 3, 5, 7, 9], 5, 0, 4), 2)

    def test_nonexistent_target(self):
        self.assertEqual(biSearchFromTo([1, 3, 5, 7, 9], 6, 0, 4), -4)

    def test_empty_array(self):
        self.assertEqual(biSearchFromTo([], 5, 0, 0), -1)

    def test_single_element_array(self):
        self.assertEqual(biSearchFromTo([5], 5, 0, 0), 0)

if __name__ == "__main__":
    unittest.main()

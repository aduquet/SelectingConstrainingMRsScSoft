import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.clip import clip

class TestClip(unittest.TestCase):
    def test_clip(self):
        self.assertEqual(clip([1, 2, 3, 4, 5], 2, 4), [2, 2, 3, 4, 4])

    def test_empty_list(self):
        self.assertEqual(clip([], 1, 10), [])

    def test_no_clipping(self):
        self.assertEqual(clip([2, 3, 4], 1, 5), [2, 3, 4])

    def test_all_clipped(self):
        self.assertEqual(clip([0, 6], 1, 5), [1, 5])

if __name__ == "__main__":
    unittest.main()

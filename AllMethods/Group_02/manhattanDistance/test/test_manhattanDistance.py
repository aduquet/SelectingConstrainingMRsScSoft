import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.manhattanDistance import manhattanDistance
class TestManhattanDistance(unittest.TestCase):
    def test_manhattan_distance(self):
        self.assertEqual(manhattanDistance([1, 2, 3], [4, 5, 6]), 9)

    def test_mismatched_dimensions(self):
        with self.assertRaises(ValueError):
            manhattanDistance([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

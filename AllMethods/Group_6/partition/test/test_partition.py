import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))

from src.partition import partition

import unittest

class TestPartitionFunction(unittest.TestCase):

    def test_basic_partition(self):
        work = [3, 2, 5, 4, 1]
        pivot = partition(work, 0, len(work), 2)
        self.assertEqual(pivot, 2)
        self.assertEqual(work, [2, 1, 3, 5, 4])

    def test_empty_list(self):
        work = []
        with self.assertRaises(IndexError):
            partition(work, 0, len(work), 0)

    def test_single_element(self):
        work = [1]
        pivot = partition(work, 0, len(work), 0)
        self.assertEqual(pivot, 0)
        self.assertEqual(work, [1])

    def test_all_equal_elements(self):
        work = [5, 5, 5, 5, 5]
        pivot = partition(work, 0, len(work), 2)
        self.assertEqual(pivot, 4)
        self.assertEqual(work, [5, 5, 5, 5, 5])

# Running the tests
unittest.main(argv=[''], exit=False)

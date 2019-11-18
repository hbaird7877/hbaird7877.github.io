import unittest
from binary_search import binary_search

class BinarySearch(unittest.TestCase):
    '''tests for binary_search.py'''

    def test_checks_first_array_index(self):
        self.assertEqual(binary_search(1, [1,2,3,4,5]), 0)
    def test_checks_second_array_index(self):
        self.assertEqual(binary_search(2, [1,2,3,4,5]), 1)
    def test_checks_middle_array_index(self):
        self.assertEqual(binary_search(3, [1,2,3,4,5]), 2)
    def test_checks_last_array_index(self):
        self.assertEqual(binary_search(5, [1,2,3,4,5]), 4)
    def test_checks_not_found(self):
        self.assertEqual(binary_search(6, [1,2,3,4,5]), -1)

if __name__ == '__main__':
    unittest.main()
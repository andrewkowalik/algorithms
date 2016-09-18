import unittest

from binary_search import binary_search

class BinarySearchTestCase(unittest.TestCase):

    def test_search_lower_half(self):
        test_list = [1, 3, 6, 7, 8, 9]
        item = 3
        
        result = binary_search(test_list, item)

        self.assertEqual(item, result)

    def test_search_upper_half(self):
        test_list = [1, 3, 6, 7, 8, 10]
        item = 8

        result = binary_search(test_list, item)

        self.assertEqual(item, result)

    def test_search_middle(self):
        test_list = [1, 3, 6, 7, 8]
        item = 6

        result = binary_search(test_list, item)

        self.assertEqual(item, result)

    def test_search_missing(self):
        test_list = [1, 3, 6, 7, 8]
        item = -5

        result = binary_search(test_list, item)

        self.assertIsNone(result)

    def test_search_beginning_of_list(self):
        test_list = [1, 3, 5, 6, 7, 8]
        item = 1

        result = binary_search(test_list, item)

        self.assertEqual(item, result)

    def test_search_end_of_list(self):
        test_list = [1, 3, 5, 6, 7, 8]
        item = 8

        result = binary_search(test_list, item)

        self.assertEqual(item, result)

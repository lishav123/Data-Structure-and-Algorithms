import unittest
from bubble_sort import Sorting

class TestBubbleSort(unittest.TestCase):
    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        Sorting.bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        Sorting.bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_duplicates(self):
        arr = [3, 1, 2, 3, 1]
        Sorting.bubble_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        arr = [-2, -5, -1, -3]
        Sorting.bubble_sort(arr)
        self.assertEqual(arr, [-5, -3, -2, -1])

    def test_mixed_numbers(self):
        arr = [0, -1, 3, -2, 2]
        Sorting.bubble_sort(arr)
        self.assertEqual(arr, [-2, -1, 0, 2, 3])

    def test_single_element(self):
        arr = [42]
        Sorting.bubble_sort(arr)
        self.assertEqual(arr, [42])

    def test_empty_list(self):
        arr = []
        Sorting.bubble_sort(arr)
        self.assertEqual(arr, [])

    def test_large_numbers(self):
        arr = [100000, 99999, 100001]
        Sorting.bubble_sort(arr)
        self.assertEqual(arr, [99999, 100000, 100001])

    def test_all_same_elements(self):
        arr = [7, 7, 7, 7]
        Sorting.bubble_sort(arr)
        self.assertEqual(arr, [7, 7, 7, 7])

    def test_floats(self):
        arr = [3.2, 1.5, 2.8, 1.5]
        Sorting.bubble_sort(arr)
        self.assertEqual(arr, [1.5, 1.5, 2.8, 3.2])
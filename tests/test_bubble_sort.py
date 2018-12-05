import os
import unittest
from algorithms.algorithms.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        number_array = [1, 2, 7, 9, 3, 23, 1, 0, 6, 8]

        sorted_array = [0, 1, 1, 2, 3, 6, 7, 8, 9, 23]
        bubbled = bubble_sort(number_array)
        self.assertEqual(bubbled, sorted_array)

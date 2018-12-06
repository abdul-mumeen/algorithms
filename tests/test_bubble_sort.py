from utils import BaseTestClass
from algorithms.algorithms.bubble_sort import bubble_sort


class TestBubbleSort(BaseTestClass):

    def test_bubble_sort(self):
        bubbled_list = bubble_sort(self.test_number_list)
        self.assertEqual(bubbled_list, self.expected_list)

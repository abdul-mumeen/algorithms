from utils import BaseTestClass
from algorithms.quick_sort import quick_sort


class TestQuickSort(BaseTestClass):

    def test_quick_sort(self):
        sorted_list = quick_sort(self.test_number_list)
        self.assertEqual(sorted_list, self.expected_list)

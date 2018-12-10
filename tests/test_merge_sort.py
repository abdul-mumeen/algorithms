from utils import BaseTestClass
from algorithms.algorithms.merge_sort import merge_sort


class TestMergeSort(BaseTestClass):

    def test_merge_sort(self):
        sorted_list = merge_sort(self.test_number_list)
        self.assertEqual(sorted_list, self.expected_list)

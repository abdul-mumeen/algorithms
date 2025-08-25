from utils import BaseTestClass
from algorithms.insertion_sort import insertion_sort


class TestInsertionSort(BaseTestClass):

    def test_insertion_sort(self):
        sorted_list = insertion_sort(self.test_number_list)
        self.assertEqual(sorted_list, self.expected_list)

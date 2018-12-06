from utils import BaseTestClass
from algorithms.algorithms.insertion_sort import insertion_sort


class TestInsertionSort(BaseTestClass):

    def test_insertion_sort(self):
        bubbled_list = insertion_sort(self.test_number_list)
        self.assertEqual(bubbled_list, self.expected_list)

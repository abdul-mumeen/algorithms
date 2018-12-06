"""Base class to include test array and expected result"""

import unittest


class BaseTestClass(unittest.TestCase):

    def setUp(self):
        self.test_number_list = [1, 2, 7, 9, 3, 23, 1, 0, 6, 8]
        self.expected_list = [0, 1, 1, 2, 3, 6, 7, 8, 9, 23]

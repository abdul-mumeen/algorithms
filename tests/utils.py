"""Base class to include test array and expected result"""

import unittest
from collections import defaultdict


class BaseTestClass(unittest.TestCase):

    def setUp(self):
        self.test_number_list = [1, 2, 7, 9, 3, 23, 1, 0, 6, 8]
        self.expected_list = [0, 1, 1, 2, 3, 6, 7, 8, 9, 23]


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)
        self.addEdge(0, 1)
        self.addEdge(0, 2)
        self.addEdge(1, 2)
        self.addEdge(2, 0)
        self.addEdge(2, 3)
        self.addEdge(3, 3)

    def addEdge(self, parent_vertex, child_vertex):
        self.graph[parent_vertex].append(child_vertex)

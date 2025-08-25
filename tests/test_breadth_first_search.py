import unittest
from utils import Graph
from algorithms.breadth_first_search import breadth_first_search


class TestBreadthFirstSearch(unittest.TestCase):

    def test_breadth_first_search(self):
        graph = Graph()
        expected_output_sequence = [2, 0, 3, 1]
        output = breadth_first_search(graph, 2)
        self.assertListEqual(output, expected_output_sequence)

import unittest
from utils import Graph
from algorithms.algorithms.depth_first_search import depth_first_search


class TestDepthFirstSearch(unittest.TestCase):

    def test_depth_first_search(self):
        graph = Graph()
        expected_output_sequence = [2, 0, 1, 3]
        output = depth_first_search(graph, 2)
        self.assertListEqual(output, expected_output_sequence)

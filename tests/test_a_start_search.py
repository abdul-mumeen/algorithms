import unittest

from algorithms.a_star_search import a_star_search
from algorithms.a_star_search_util import SquareGridWithWeight


class TestBreadthFirstSearch(unittest.TestCase):
    def test_a_star_search(self):
        grid = SquareGridWithWeight(3, 3)
        grid.walls = [(0, 1), (0, 2)]
        grid.weights = {loc: 5 for loc in [(0, 0), (1, 0),
                                           (2, 0), (2, 1), (2, 2)]}

        start, goal = (0, 0), (2, 2)
        came_from, cost_so_far = a_star_search(grid, start, goal)
        expected_path = {(0, 0): None, (1, 0): (0, 0), (2, 0): (1, 0), (1, 1): (1, 0), (1, 2): (1, 1), (2, 1): (1, 1), (2, 2): (1, 2)}
        expected_cost = {(0, 0): 0, (1, 0): 5, (2, 0): 10, (1, 1): 6, (1, 2): 7, (2, 1): 11, (2, 2): 12}
        self.assertEqual(came_from, expected_path)
        self.assertEqual(cost_so_far, expected_cost)

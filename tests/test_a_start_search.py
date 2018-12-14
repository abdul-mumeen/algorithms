import unittest

from algorithms.algorithms.a_star_search import a_star_search
from algorithms.algorithms.a_star_search_util import SquareGridWithWeight


class TestBreadthFirstSearch(unittest.TestCase):
    def test_a_star_search(self):
        grid = SquareGridWithWeight(10, 10)
        grid.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
        grid.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                           (4, 3), (4, 4), (4, 5), (4, 6),
                                           (4, 7), (4, 8), (5, 1), (5, 2),
                                           (5, 3), (5, 4), (5, 5), (5, 6),
                                           (5, 7), (5, 8), (6, 2), (6, 3),
                                           (6, 4), (6, 5), (6, 6), (6, 7),
                                           (7, 3), (7, 4), (7, 5)]}

        start, goal = (1, 4), (7, 8)
        came_from, cost_so_far = a_star_search(grid, start, goal)
        print(came_from, 'check out', cost_so_far)
        self.assertTrue(False)

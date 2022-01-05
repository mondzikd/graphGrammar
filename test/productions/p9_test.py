import unittest

import networkx as nx

from productions.p9 import p9


class P9TestCase(unittest.TestCase):
    def test_p9_simple(self):
        # given
        graph = nx.Graph()
        x1, y1 = 3, 5
        x2, y2 = 3, 1
        x3 = (x1 + x2) / 2.0
        y3 = (y1 + y2) / 2.0
        graph.add_nodes_from(
            [
                (0, {"label": "E", "pos": (3, 7)}),
                (1, {"label": "i", "pos": (2, 6)}),
                (2, {"label": "i", "pos": (4, 6)}),
                (3, {"label": "I", "pos": (1, 4)}),
                (4, {"label": "I", "pos": (1, 2)}),
                (5, {"label": "I", "pos": (5, 4)}),
                (6, {"label": "I", "pos": (5, 2)}),
                (7, {"label": "E", "pos": (x1, y1)}),
                (8, {"label": "E", "pos": (x3, y3)}),
                (9, {"label": "E", "pos": (x3, y3)}),
                (10, {"label": "E", "pos": (x2, y2)}),
            ]
        )
        graph.add_edges_from(
            [
                (0, 1),
                (0, 2),
                (1, 3),
                (1, 4),
                (2, 5),
                (2, 6),
                (3, 7),
                (3, 8),
                (4, 8),
                (4, 10),
                (5, 7),
                (5, 9),
                (6, 9),
                (6, 10),
                (7, 8),
                (7, 9),
                (8, 10),
                (9, 10),
            ]
        )

        # when
        p9(graph)

        # then
        expected_graph = nx.Graph()
        expected_graph.add_nodes_from(
            [
                (0, {"label": "E", "pos": (3, 7)}),
                (1, {"label": "i", "pos": (2, 6)}),
                (2, {"label": "i", "pos": (4, 6)}),
                (3, {"label": "I", "pos": (1, 4)}),
                (4, {"label": "I", "pos": (1, 2)}),
                (5, {"label": "I", "pos": (5, 2)}),
                (6, {"label": "I", "pos": (5, 4)}),
                (7, {"label": "E", "pos": (x1, y1)}),
                (8, {"label": "E", "pos": (x3, y3)}),
                (9, {"label": "E", "pos": (x2, y2)}),
            ]
        )
        expected_graph.add_edges_from(
            [
                (0, 1),
                (0, 2),
                (1, 3),
                (1, 4),
                (2, 5),
                (2, 6),
                (3, 7),
                (3, 8),
                (4, 8),
                (4, 9),
                (5, 7),
                (5, 8),
                (6, 8),
                (6, 9),
                (7, 8),
                (8, 9),
            ]
        )

        self.assertTrue(nx.is_isomorphic(graph, expected_graph))


if __name__ == "__main__":
    unittest.main()
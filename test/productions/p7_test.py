import unittest

import networkx as nx

from productions.p7 import p7, generate_p7_left_side_graph
from strategies.super_simple_strategy import super_simple_strategy


class P7Test(unittest.TestCase):

    def test_simple_example(self):
        # given
        graph = nx.Graph()
        graph.graph["max_level"] = 3
        graph.add_nodes_from([
            (0, {"label": "E", "level": 1, "color": "green", "pos": (10, 10)}),
            (1, {"label": "i", "level": 2, "color": "brown", "pos": (9, 9)}),
            (2, {"label": "i", "level": 2, "color": "brown", "pos": (11, 9)}),
            (3, {"label": "I", "level": 3, "color": "grey", "pos": (8, 6)}),
            (4, {"label": "I", "level": 3, "color": "grey", "pos": (12, 6)}),
            (5, {"label": "I", "level": 3, "color": "grey", "pos": (12, 4)}),
            (6, {"label": "I", "level": 3, "color": "grey", "pos": (8, 4)}),
            (7, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (8, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (9, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (10, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (11, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)}),
            (12, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)})
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (1, 3),
            (1, 6),
            (2, 4), (2, 5),
            (3, 7), (3, 9),
            (6, 9), (6, 11),
            (4, 8), (4, 10),
            (5, 10), (5, 12),
            (7, 9), (9, 11),
            (8, 10), (10, 12)
        ])

        result_graph = nx.Graph()
        result_graph.add_nodes_from([
            (0, {"label": "E", "level": 1, "color": "green", "pos": (10, 10)}),
            (1, {"label": "i", "level": 2, "color": "brown", "pos": (9, 9)}),
            (2, {"label": "i", "level": 2, "color": "brown", "pos": (11, 9)}),
            (3, {"label": "I", "level": 3, "color": "grey", "pos": (8, 6)}),
            (4, {"label": "I", "level": 3, "color": "grey", "pos": (12, 6)}),
            (5, {"label": "I", "level": 3, "color": "grey", "pos": (12, 4)}),
            (6, {"label": "I", "level": 3, "color": "grey", "pos": (8, 4)}),
            (7, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (9, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (11, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)}),
        ])

        result_graph.add_edges_from([
            (0, 1), (0, 2), (1, 3),
            (1, 6),
            (2, 4), (2, 5),
            (3, 7), (3, 9),
            (6, 9), (6, 11),
            (4, 7), (4, 9),
            (5, 9), (5, 11),
            (7, 9), (9, 11),
        ])

        # when
        p7(graph, super_simple_strategy(graph, generate_p7_left_side_graph()))

        # then
        self.assertEqual(len(graph.nodes()), 10)
        self.assertEqual(len(graph.edges()), 16)
        self.assertTrue(nx.is_isomorphic(graph, result_graph))

    def test_complex_graph(self):
        # given
        graph = nx.Graph()
        graph.graph["max_level"] = 3
        graph.add_nodes_from([
            (0, {"label": "E", "level": 1, "color": "green", "pos": (10, 10)}),
            (1, {"label": "i", "level": 2, "color": "brown", "pos": (9, 9)}),
            (2, {"label": "i", "level": 2, "color": "brown", "pos": (11, 9)}),
            (3, {"label": "I", "level": 3, "color": "grey", "pos": (8, 6)}),
            (4, {"label": "I", "level": 3, "color": "grey", "pos": (12, 6)}),
            (5, {"label": "I", "level": 3, "color": "grey", "pos": (12, 4)}),
            (6, {"label": "I", "level": 3, "color": "grey", "pos": (8, 4)}),
            (7, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (8, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (9, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (10, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (11, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)}),
            (12, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)}),
            (13, {"label": "E", "level": 3, "color": "blue", "pos": (2, 2)}),
            (14, {"label": "E", "level": 3, "color": "blue", "pos": (14, 9)})
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (1, 3),
            (1, 6),
            (2, 4), (2, 5),
            (3, 7), (3, 9),
            (6, 9), (6, 11),
            (4, 8), (4, 10),
            (5, 10), (5, 12),
            (7, 9), (9, 11),
            (8, 10), (10, 12),
            (13, 6), (14, 5)
        ])

        result_graph = nx.Graph()
        result_graph.add_nodes_from([
            (0, {"label": "E", "level": 1, "color": "green", "pos": (10, 10)}),
            (1, {"label": "i", "level": 2, "color": "brown", "pos": (9, 9)}),
            (2, {"label": "i", "level": 2, "color": "brown", "pos": (11, 9)}),
            (3, {"label": "I", "level": 3, "color": "grey", "pos": (8, 6)}),
            (4, {"label": "I", "level": 3, "color": "grey", "pos": (12, 6)}),
            (5, {"label": "I", "level": 3, "color": "grey", "pos": (12, 4)}),
            (6, {"label": "I", "level": 3, "color": "grey", "pos": (8, 4)}),
            (7, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (9, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (11, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)}),
            (13, {"label": "E", "level": 3, "color": "blue", "pos": (2, 2)}),
            (14, {"label": "E", "level": 3, "color": "blue", "pos": (14, 9)})
        ])

        result_graph.add_edges_from([
            (0, 1), (0, 2), (1, 3),
            (1, 6),
            (2, 4), (2, 5),
            (3, 7), (3, 9),
            (6, 9), (6, 11),
            (4, 7), (4, 9),
            (5, 9), (5, 11),
            (7, 9), (9, 11),
            (13, 6), (14, 5)
        ])

        # when
        p7(graph, super_simple_strategy(graph, generate_p7_left_side_graph()))

        # then
        self.assertEqual(len(graph.nodes()), 12)
        self.assertEqual(len(graph.edges()), 18)
        self.assertTrue(nx.is_isomorphic(graph, result_graph))

    def test_different_position(self):
        # given
        graph = nx.Graph()
        graph.graph["max_level"] = 3
        graph.add_nodes_from([
            (0, {"label": "E", "level": 1, "color": "green", "pos": (10, 10)}),
            (1, {"label": "i", "level": 2, "color": "brown", "pos": (9, 9)}),
            (2, {"label": "i", "level": 2, "color": "brown", "pos": (11, 9)}),
            (3, {"label": "I", "level": 3, "color": "grey", "pos": (8, 6)}),
            (4, {"label": "I", "level": 3, "color": "grey", "pos": (12, 6)}),
            (5, {"label": "I", "level": 3, "color": "grey", "pos": (12, 4)}),
            (6, {"label": "I", "level": 3, "color": "grey", "pos": (8, 4)}),
            (7, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (8, {"label": "E", "level": 3, "color": "blue", "pos": (10, 6)}),
            (9, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (10, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (11, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)}),
            (12, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)})
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (1, 3),
            (1, 6),
            (2, 4), (2, 5),
            (3, 7), (3, 9),
            (6, 9), (6, 11),
            (4, 8), (4, 10),
            (5, 10), (5, 12),
            (7, 9), (9, 11),
            (8, 10), (10, 12)
        ])

        # when
        left_side = generate_p7_left_side_graph()
        with self.assertRaises(Exception):
            p7(graph, super_simple_strategy(graph, left_side))

    def test_different_label(self):
        # given
        graph = nx.Graph()
        graph.graph["max_level"] = 3
        graph.add_nodes_from([
            (0, {"label": "E", "level": 1, "color": "green", "pos": (10, 10)}),
            (1, {"label": "i", "level": 2, "color": "brown", "pos": (9, 9)}),
            (2, {"label": "i", "level": 2, "color": "brown", "pos": (11, 9)}),
            (3, {"label": "I", "level": 3, "color": "grey", "pos": (8, 6)}),
            (4, {"label": "I", "level": 3, "color": "grey", "pos": (12, 6)}),
            (5, {"label": "I", "level": 3, "color": "grey", "pos": (12, 4)}),
            (6, {"label": "I", "level": 3, "color": "grey", "pos": (8, 4)}),
            (7, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (8, {"label": "A", "level": 3, "color": "blue", "pos": (10, 7)}),
            (9, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (10, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (11, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)}),
            (12, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)})
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (1, 3),
            (1, 6),
            (2, 4), (2, 5),
            (3, 7), (3, 9),
            (6, 9), (6, 11),
            (4, 8), (4, 10),
            (5, 10), (5, 12),
            (7, 9), (9, 11),
            (8, 10), (10, 12)
        ])

        # when then
        with self.assertRaises(IndexError):
            p7(graph, super_simple_strategy(graph, generate_p7_left_side_graph()))

    def test_missing_nodes(self):
        # given
        graph = nx.Graph()
        graph.graph["max_level"] = 3
        graph.add_nodes_from([
            (1, {"label": "i", "level": 2, "color": "brown", "pos": (9, 9)}),
            (2, {"label": "i", "level": 2, "color": "brown", "pos": (11, 9)}),
            (3, {"label": "I", "level": 3, "color": "grey", "pos": (8, 6)}),
            (4, {"label": "I", "level": 3, "color": "grey", "pos": (12, 6)}),
            (5, {"label": "I", "level": 3, "color": "grey", "pos": (12, 4)}),
            (6, {"label": "I", "level": 3, "color": "grey", "pos": (8, 4)}),
            (7, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (8, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (9, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (10, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (11, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)}),
            (12, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)})
        ])

        graph.add_edges_from([
            (1, 3),
            (1, 6),
            (2, 4), (2, 5),
            (3, 7), (3, 9),
            (6, 9), (6, 11),
            (4, 8), (4, 10),
            (5, 10), (5, 12),
            (7, 9), (9, 11),
            (8, 10), (10, 12)
        ])
        # when then
        with self.assertRaises(IndexError):
            p7(graph, super_simple_strategy(graph, generate_p7_left_side_graph()))

    def test_missing_edges(self):
        # given
        graph = nx.Graph()
        graph.graph["max_level"] = 3
        graph.add_nodes_from([
            (0, {"label": "E", "level": 1, "color": "green", "pos": (10, 10)}),
            (1, {"label": "i", "level": 2, "color": "brown", "pos": (9, 9)}),
            (2, {"label": "i", "level": 2, "color": "brown", "pos": (11, 9)}),
            (3, {"label": "I", "level": 3, "color": "grey", "pos": (8, 6)}),
            (4, {"label": "I", "level": 3, "color": "grey", "pos": (12, 6)}),
            (5, {"label": "I", "level": 3, "color": "grey", "pos": (12, 4)}),
            (6, {"label": "I", "level": 3, "color": "grey", "pos": (8, 4)}),
            (7, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (8, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
            (9, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (10, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
            (11, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)}),
            (12, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)})
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (1, 3),
            (1, 6),
            (2, 4), (2, 5),
            (3, 7), (3, 9),
            (6, 9), (6, 11),
            (4, 10),
            (5, 10), (5, 12),
            (7, 9), (9, 11),
            (8, 10)
        ])

        # when then
        with self.assertRaises(IndexError):
            p7(graph, super_simple_strategy(graph, generate_p7_left_side_graph()))

    def test_invalid_position(self):
        pass


if __name__ == '__main__':
    unittest.main()

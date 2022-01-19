import unittest

import networkx as nx

from productions.p7 import p7, generate_p7_left_side_graph
from strategies.super_simple_strategy import super_simple_strategy


class P7Test(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

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
        graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (4, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (5, {"label": "E", "color": "blue", "level": 0, "pos": (2, 1)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (4, 1)})
        ])
        graph.add_edges_from([
            (1, 2), (1, 4), (1, 6), (1, 8),
            (2, 3), (2, 6), (2, 7),
            (3, 7),
            (4, 5), (4, 8), (4, 9),
            (5, 9)
        ])

        # when
        p8(graph)

        # then
        self.assertEqual(len(graph.nodes()), 9)
        self.assertEqual(len(graph.edges()), 12)

    def test_different_label(self):
        # given
        graph = nx.Graph()
        graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (4, {"label": "I", "color": "blue", "level": 0, "pos": (2, 2)}),
            (5, {"label": "E", "color": "blue", "level": 0, "pos": (2, 1)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (4, 1)})
        ])
        graph.add_edges_from([
            (1, 2), (1, 4), (1, 6), (1, 8),
            (2, 3), (2, 6), (2, 7),
            (3, 7),
            (4, 5), (4, 8), (4, 9),
            (5, 9)
        ])

        # when
        p8(graph)

        # then
        self.assertEqual(len(graph.nodes()), 9)
        self.assertEqual(len(graph.edges()), 12)

    def test_different_level_without_matching_graph(self):
        # given
        graph = nx.Graph()
        graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 1, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 1, "pos": (2, 0)}),
            (4, {"label": "I", "color": "blue", "level": 1, "pos": (2, 2)}),
            (5, {"label": "E", "color": "blue", "level": 1, "pos": (2, 1)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (4, 1)})
        ])
        graph.add_edges_from([
            (1, 2), (1, 4), (1, 6), (1, 8),
            (2, 3), (2, 6), (2, 7),
            (3, 7),
            (4, 5), (4, 8), (4, 9),
            (5, 9)
        ])

        # when
        p8(graph)

        # then
        self.assertEqual(len(graph.nodes()), 9)
        self.assertEqual(len(graph.edges()), 12)

    def test_different_level_with_matching_graph(self):
        # given
        graph = nx.Graph()
        graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 1, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 1, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 1, "pos": (2, 0)}),
            (4, {"label": "E", "color": "blue", "level": 1, "pos": (2, 2)}),
            (5, {"label": "E", "color": "blue", "level": 1, "pos": (2, 0)}),
            (6, {"label": "I", "color": "brown", "level": 1, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 1, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 1, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 1, "pos": (4, 1)}),
            (10, {"label": "I", "color": "brown", "level": 0, "pos": (5, 7)}),
            (11, {"label": "I", "color": "brown", "level": 0, "pos": (6, 8)}),
            (12, {"label": "I", "color": "brown", "level": 0, "pos": (7, 9)})
        ])
        graph.add_edges_from([
            (1, 2), (1, 4), (1, 6), (1, 8), (1, 11),
            (2, 3), (2, 6), (2, 7), (2, 12),
            (3, 7),
            (4, 5), (4, 8), (4, 9),
            (5, 9), (5, 10),

        ])

        result_graph = nx.Graph(max_id=0, max_level=0)
        result_graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 1, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 1, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 1, "pos": (2, 0)}),
            (6, {"label": "I", "color": "brown", "level": 1, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 1, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 1, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 1, "pos": (4, 1)}),
            (10, {"label": "I", "color": "brown", "level": 0, "pos": (5, 7)}),
            (11, {"label": "I", "color": "brown", "level": 0, "pos": (6, 8)}),
            (12, {"label": "I", "color": "brown", "level": 0, "pos": (7, 9)})
        ])
        result_graph.add_edges_from([
            (1, 2), (1, 6), (1, 8), (1, 11),
            (2, 3), (2, 6), (2, 7), (2, 8), (2, 9), (2, 12),
            (3, 7), (3, 9), (3, 10),
        ])

        # when
        p8(graph)

        # then
        self.assertEqual(len(graph.nodes()), 10)
        self.assertEqual(len(graph.edges()), 13)
        self.assertTrue(nx.is_isomorphic(graph, result_graph))

    def test_different_level_with_matching_graph_on_lower_level(self):
        # given
        graph = nx.Graph()
        graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (4, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (5, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (4, 1)}),
            (10, {"label": "I", "color": "brown", "level": 1, "pos": (5, 7)}),
            (11, {"label": "I", "color": "brown", "level": 1, "pos": (6, 8)}),
            (12, {"label": "I", "color": "brown", "level": 1, "pos": (7, 9)})
        ])
        graph.add_edges_from([
            (1, 2), (1, 4), (1, 6), (1, 8), (1, 11),
            (2, 3), (2, 6), (2, 7), (2, 12),
            (3, 7),
            (4, 5), (4, 8), (4, 9),
            (5, 9), (5, 10),

        ])

        result_graph = nx.Graph()
        result_graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (4, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (5, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (4, 1)}),
            (10, {"label": "I", "color": "brown", "level": 1, "pos": (5, 7)}),
            (11, {"label": "I", "color": "brown", "level": 1, "pos": (6, 8)}),
            (12, {"label": "I", "color": "brown", "level": 1, "pos": (7, 9)})
        ])
        result_graph.add_edges_from([
            (1, 2), (1, 4), (1, 6), (1, 8), (1, 11),
            (2, 3), (2, 6), (2, 7), (2, 12),
            (3, 7),
            (4, 5), (4, 8), (4, 9),
            (5, 9), (5, 10),
        ])

        # when
        p8(graph)

        # then
        self.assertEqual(len(graph.nodes()), 12)
        self.assertEqual(len(graph.edges()), 15)
        self.assertTrue(nx.is_isomorphic(graph, result_graph))

    def test_horizontal(self):
        # given
        graph = nx.Graph()
        graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (4, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (5, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (4, 1)})
        ])
        graph.add_edges_from([
            (1, 2), (1, 4), (1, 6), (1, 8),
            (2, 3), (2, 6), (2, 7),
            (3, 7),
            (4, 5), (4, 8), (4, 9),
            (5, 9)
        ])

        # when
        p8(graph, strategy=Strategy.HORIZONTAL)

        # then
        self.assertEqual(len(graph.nodes()), 9)
        self.assertEqual(len(graph.edges()), 12)

    def test_apply_number(self):
        # given
        graph = nx.Graph(max_level=0)
        graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (4, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (5, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (4, 1)}),
            (10, {"label": "E", "color": "green", "level": 0, "pos": (9, 11)}),
            (11, {"label": "E", "color": "green", "level": 0, "pos": (9, 9)}),
            (12, {"label": "E", "color": "green", "level": 0, "pos": (9, 7)}),
            (13, {"label": "E", "color": "green", "level": 0, "pos": (9, 9)}),
            (14, {"label": "E", "color": "green", "level": 0, "pos": (9, 7)}),
            (15, {"label": "I", "color": "red", "level": 0, "pos": (8, 10)}),
            (16, {"label": "I", "color": "red", "level": 0, "pos": (8, 8)}),
            (17, {"label": "I", "color": "red", "level": 0, "pos": (10, 10)}),
            (18, {"label": "I", "color": "red", "level": 0, "pos": (10, 8)}),
            (19, {"label": "E", "color": "green", "level": 0, "pos": (10, 11)}),
        ])
        graph.add_edges_from([
            (1, 2), (1, 4), (1, 6), (1, 8),
            (2, 3), (2, 6), (2, 7),
            (3, 7),
            (4, 5), (4, 8), (4, 9),
            (5, 9),
            (10, 11), (10, 13), (10, 15), (10, 17), (10, 19),
            (11, 12), (11, 15), (11, 16),
            (12, 16),
            (13, 14), (13, 17), (13, 18),
            (14, 18)
        ])

        result_graph = nx.Graph(max_level=0)
        result_graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (4, 1)}),
            (10, {"label": "E", "color": "green", "level": 0, "pos": (9, 11)}),
            (11, {"label": "E", "color": "green", "level": 0, "pos": (9, 9)}),
            (12, {"label": "E", "color": "green", "level": 0, "pos": (9, 7)}),
            (13, {"label": "E", "color": "green", "level": 0, "pos": (9, 9)}),
            (14, {"label": "E", "color": "green", "level": 0, "pos": (9, 7)}),
            (15, {"label": "I", "color": "red", "level": 0, "pos": (8, 10)}),
            (16, {"label": "I", "color": "red", "level": 0, "pos": (8, 8)}),
            (17, {"label": "I", "color": "red", "level": 0, "pos": (10, 10)}),
            (18, {"label": "I", "color": "red", "level": 0, "pos": (10, 8)}),
            (19, {"label": "E", "color": "green", "level": 0, "pos": (10, 11)}),
        ])
        result_graph.add_edges_from([
            (1, 2), (1, 6), (1, 8),
            (2, 3), (2, 6), (2, 7), (2, 8), (2, 9),
            (3, 7), (3, 9),
            (10, 11), (10, 13), (10, 15), (10, 17), (10, 19),
            (11, 12), (11, 15), (11, 16),
            (12, 16),
            (13, 14), (13, 17), (13, 18),
            (14, 18)
        ])

        visualize(graph, level=0)

        # when
        p8(graph, n=1)
        visualize(graph, level=0)

        # then
        self.assertEqual(len(graph.nodes()), 17)
        self.assertEqual(len(graph.edges()), 23)
        self.assertTrue(nx.is_isomorphic(graph, result_graph))

    def test_horizontal2(self):
        # given
        graph = nx.Graph(max_level=0)
        graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (0, 2)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (4, 2)}),
            (4, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (5, {"label": "E", "color": "blue", "level": 0, "pos": (4, 2)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (1, 0)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (3, 0)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (1, 4)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (3, 4)}),
            (10, {"label": "E", "color": "green", "level": 0, "pos": (2, 10)}),
            (11, {"label": "E", "color": "green", "level": 0, "pos": (2, 8)}),
            (12, {"label": "E", "color": "green", "level": 0, "pos": (2, 6)}),
            (13, {"label": "E", "color": "green", "level": 0, "pos": (2, 8)}),
            (14, {"label": "E", "color": "green", "level": 0, "pos": (2, 6)}),
            (15, {"label": "I", "color": "red", "level": 0, "pos": (1, 9)}),
            (16, {"label": "I", "color": "red", "level": 0, "pos": (1, 7)}),
            (17, {"label": "I", "color": "red", "level": 0, "pos": (3, 9)}),
            (18, {"label": "I", "color": "red", "level": 0, "pos": (3, 7)}),
        ])
        graph.add_edges_from([
            (1, 2), (1, 4), (1, 6), (1, 8),
            (2, 3), (2, 6), (2, 7),
            (3, 7),
            (4, 5), (4, 8), (4, 9),
            (5, 9),
            (10, 11), (10, 13), (10, 15), (10, 17),
            (11, 12), (11, 15), (11, 16),
            (12, 16),
            (13, 14), (13, 17), (13, 18),
            (14, 18)
        ])

        result_graph = nx.Graph(max_level=0)
        result_graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (0, 2)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (4, 2)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (1, 0)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (3, 0)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (1, 4)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (3, 4)}),
            (10, {"label": "E", "color": "green", "level": 0, "pos": (2, 10)}),
            (11, {"label": "E", "color": "green", "level": 0, "pos": (2, 8)}),
            (12, {"label": "E", "color": "green", "level": 0, "pos": (2, 6)}),
            (13, {"label": "E", "color": "green", "level": 0, "pos": (2, 8)}),
            (14, {"label": "E", "color": "green", "level": 0, "pos": (2, 6)}),
            (15, {"label": "I", "color": "red", "level": 0, "pos": (1, 9)}),
            (16, {"label": "I", "color": "red", "level": 0, "pos": (1, 7)}),
            (17, {"label": "I", "color": "red", "level": 0, "pos": (3, 9)}),
            (18, {"label": "I", "color": "red", "level": 0, "pos": (3, 7)}),
        ])
        result_graph.add_edges_from([
            (1, 2), (1, 6), (1, 8),
            (2, 3), (2, 6), (2, 7), (2, 8), (2, 9),
            (3, 7), (3, 9),
            (10, 11), (10, 13), (10, 15), (10, 17),
            (11, 12), (11, 15), (11, 16),
            (12, 16),
            (13, 14), (13, 17), (13, 18),
            (14, 18)
        ])

        # visualize(graph, level=0)
        # when
        p8(graph, strategy=Strategy.HORIZONTAL)
        # visualize(graph, level=0)

        # then
        self.assertEqual(len(graph.nodes()), 16)
        self.assertEqual(len(graph.edges()), 22)
        self.assertTrue(nx.is_isomorphic(graph, result_graph))

if __name__ == '__main__':
    unittest.main()

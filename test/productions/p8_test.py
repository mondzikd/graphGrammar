import unittest
import networkx as nx

from productions.p8 import p8


class TestProduction8(unittest.TestCase):
    def test_simple_example(self):
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

        result_graph = nx.Graph()
        result_graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (4, 1)}),
        ])
        result_graph.add_edges_from([
            (1, 2), (1, 6), (1, 8),
            (2, 3), (2, 6), (2, 7), (2, 8), (2, 9),
            (3, 7), (3, 9)
        ])

        # when
        p8(graph)

        # then
        self.assertEqual(len(graph.nodes()), 7)
        self.assertEqual(len(graph.edges()), 10)
        self.assertTrue(nx.is_isomorphic(graph, result_graph))

    def test_complex_graph(self):
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

        result_graph = nx.Graph()
        result_graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "level": 0, "pos": (2, 4)}),
            (2, {"label": "E", "color": "blue", "level": 0, "pos": (2, 2)}),
            (3, {"label": "E", "color": "blue", "level": 0, "pos": (2, 0)}),
            (6, {"label": "I", "color": "brown", "level": 0, "pos": (0, 3)}),
            (7, {"label": "I", "color": "brown", "level": 0, "pos": (0, 1)}),
            (8, {"label": "I", "color": "brown", "level": 0, "pos": (4, 3)}),
            (9, {"label": "I", "color": "brown", "level": 0, "pos": (4, 1)}),
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

if __name__ == '__main__':
    unittest.main()

import unittest
import networkx as nx

from productions.p3 import p3, generate_p3_left_side_graph
from strategies.p3_p4_strategy import p3_p4_strategy


class TestProduction3(unittest.TestCase):
    def test_p3(self):
        graph = nx.Graph()
        graph.add_nodes_from(
            [(1, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.4, 1.2)}),
                              (2, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (1, 1)}),
                              (3, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0, 0)}),
                              (4, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (2, 0)}),
                              (5, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.2, 0.6)}),
                              (6, {'label': 'I', 'color': 'brown', 'level': 1, 'pos': (0.85, 0.55)})
                              ]
        )

        graph.add_edges_from(
            [
                (0, 6),
                (6, 1), (6, 2), (6, 3), (6, 4),
                (2, 4), (4, 3), (3, 5), (5, 1),
                (1, 2),
            ]
        )

        result_graph = nx.Graph()
        result_graph.add_nodes_from([
            (0, {'label': 'e', 'color': 'red'}),
            (1, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.4, 1.2)}),
            (2, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (1, 1)}),
            (3, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0, 0)}),
            (4, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (2, 0)}),
            (5, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.2, 0.6)}),
            (6, {'label': 'I', 'color': 'brown', 'level': 1, 'pos': (0.85, 0.55)}),
            (8, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.4, 1.2)}),
            (9, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (1, 1)}),
            (10, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0, 0)}),
            (11, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (2, 0)}),
            (12, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.2, 0.6)}),
            (13, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.7, 1.1)}),
            (14, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (1.5, 0.5)}),
            (15, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (1.0, 0.0)}),
            (16, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.85, 0.55)}),
            (17, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (0.5375, 0.8625)}),
            (18, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (1.0125, 0.7875)}),
            (19, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (1.3375, 0.2625)}),
            (20, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (0.5125, 0.2875)}),
        ])

        result_graph.add_edges_from([
            (0, 6),
            (6, 1), (6, 2), (6, 3), (6, 4),
            (2, 4), (4, 3), (3, 5), (5, 1),
            (1, 2),
            (6, 17), (6, 18), (6, 19), (6, 20),
            (8, 12), (8, 13), (13, 16), (13, 9),
            (9, 14), (14, 16), (14, 11), (11, 15),
            (15, 16), (15, 10), (10, 12), (12, 16),
            (17, 8), (17, 13), (17, 16), (17, 12),
            (18, 13), (18, 9), (18, 14), (18, 16),
            (19, 16), (19, 14), (19, 11), (19, 15),
            (20, 12), (20, 16), (20, 15), (20, 10)
        ]
        )
        graph.graph['max_id'] = 6
        graph.graph['max_level'] = 1

        left_side = generate_p3_left_side_graph()
        p3(graph, p3_p4_strategy(graph, left_side))

        self.assertEqual(len(graph.nodes()), 20)
        self.assertEqual(len(graph.edges()), 42)
        self.assertTrue(nx.is_isomorphic(graph, result_graph))

    def test_p3_changed_center_node_position_to_proper(self):
        graph = nx.Graph()
        graph.add_nodes_from(
            [(1, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.6, 1.4)}),
                              (2, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (1, 1)}),
                              (3, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0, 0)}),
                              (4, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (2, 0)}),
                              (5, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.3, 0.7)}),
                              (6, {'label': 'I', 'color': 'brown', 'level': 1, 'pos': (0.85, 0.55)})
                              ]
        )

        graph.add_edges_from(
            [
                (0, 6),
                (6, 1), (6, 2), (6, 3), (6, 4),
                (2, 4), (4, 3), (3, 5), (5, 1),
                (1, 2),
            ]
        )

        result_graph = nx.Graph()
        result_graph.add_nodes_from([
            (0, {'label': 'e', 'color': 'red'}),
            (1, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.4, 1.2)}),
            (2, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (1, 1)}),
            (3, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0, 0)}),
            (4, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (2, 0)}),
            (5, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.2, 0.6)}),
            (6, {'label': 'I', 'color': 'brown', 'level': 1, 'pos': (0.85, 0.55)}),
            (8, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.4, 1.2)}),
            (9, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (1, 1)}),
            (10, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0, 0)}),
            (11, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (2, 0)}),
            (12, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.2, 0.6)}),
            (13, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.7, 1.1)}),
            (14, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (1.5, 0.5)}),
            (15, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (1.0, 0.0)}),
            (16, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.85, 0.55)}),
            (17, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (0.5375, 0.8625)}),
            (18, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (1.0125, 0.7875)}),
            (19, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (1.3375, 0.2625)}),
            (20, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (0.5125, 0.2875)}),
        ])

        result_graph.add_edges_from([
            (0, 6),
            (6, 1), (6, 2), (6, 3), (6, 4),
            (2, 4), (4, 3), (3, 5), (5, 1),
            (1, 2),
            (6, 17), (6, 18), (6, 19), (6, 20),
            (8, 12), (8, 13), (13, 16), (13, 9),
            (9, 14), (14, 16), (14, 11), (11, 15),
            (15, 16), (15, 10), (10, 12), (12, 16),
            (17, 8), (17, 13), (17, 16), (17, 12),
            (18, 13), (18, 9), (18, 14), (18, 16),
            (19, 16), (19, 14), (19, 11), (19, 15),
            (20, 12), (20, 16), (20, 15), (20, 10)
        ]
        )
        graph.graph['max_id'] = 6
        graph.graph['max_level'] = 1

        left_side = generate_p3_left_side_graph()
        p3(graph, p3_p4_strategy(graph, left_side))

        self.assertEqual(len(graph.nodes()), 20)
        self.assertEqual(len(graph.edges()), 42)
        self.assertTrue(nx.is_isomorphic(graph, result_graph))

    def test_p3_changed_center_node_position_to_invalid(self):
        graph = nx.Graph()
        graph.add_nodes_from(
            [(1, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.4, 1.2)}),
                              (2, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (1, 1)}),
                              (3, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0, 0)}),
                              (4, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (2, 0)}),
                              (5, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.5, 0.6)}),
                              (6, {'label': 'I', 'color': 'brown', 'level': 1, 'pos': (0.85, 0.55)})
                              ]
        )

        graph.add_edges_from(
            [
                (0, 6),
                (6, 1), (6, 2), (6, 3), (6, 4),
                (2, 4), (4, 3), (3, 5), (5, 1),
                (1, 2),
            ]
        )

        graph.graph['max_id'] = 6
        graph.graph['max_level'] = 1

        left_side = generate_p3_left_side_graph()
        with self.assertRaises(IndexError):
            p3(graph, p3_p4_strategy(graph, left_side))

    def test_p3_changed_label_to_invalid(self):
        graph = nx.Graph()
        graph.add_nodes_from(
            [(1, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.4, 1.2)}),
                              (2, {'label': 'X', 'color': 'blue', 'level': 1, 'pos': (1, 1)}),
                              (3, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0, 0)}),
                              (4, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (2, 0)}),
                              (5, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.2, 0.6)}),
                              (6, {'label': 'I', 'color': 'brown', 'level': 1, 'pos': (0.85, 0.55)})
                              ]
        )

        graph.add_edges_from(
            [
                (0, 6),
                (6, 1), (6, 2), (6, 3), (6, 4),
                (2, 4), (4, 3), (3, 5), (5, 1),
                (1, 2),
            ]
        )

        graph.graph['max_id'] = 6
        graph.graph['max_level'] = 1

        left_side = generate_p3_left_side_graph()
        with self.assertRaises(IndexError):
            p3(graph, p3_p4_strategy(graph, left_side))


    def test_p3_additional_node(self):
        graph = nx.Graph()
        graph.add_nodes_from(
            [(1, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (1, 2)}),
                              (2, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (1, 1)}),
                              (3, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0, 0)}),
                              (4, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (2, 0)}),
                              (5, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.5, 1)}),
                              (7, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (2, 2)}),
                              (6, {'label': 'I', 'color': 'brown', 'level': 1, 'pos': (0.85, 0.55)})
                              ]
        )

        graph.add_edges_from(
            [
                (0, 6),
                (6, 1), (6, 2), (6, 3), (6, 4),
                (2, 4), (4, 3), (3, 5), (5, 1),
                (1, 2),
                (6, 7),
            ]
        )

        result_graph = nx.Graph()
        result_graph.add_nodes_from([
            (0, {'label': 'e', 'color': 'red'}),
            (1, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.4, 1.2)}),
            (2, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (1, 1)}),
            (3, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0, 0)}),
            (4, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (2, 0)}),
            (5, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.2, 0.6)}),
            (6, {'label': 'I', 'color': 'brown', 'level': 1, 'pos': (0.85, 0.55)}),
            (7, {'label': 'I', 'color': 'brown', 'level': 1, 'pos': (2, 2)}),
            (8, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.4, 1.2)}),
            (9, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (1, 1)}),
            (10, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0, 0)}),
            (11, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (2, 0)}),
            (12, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.2, 0.6)}),
            (13, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.7, 1.1)}),
            (14, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (1.5, 0.5)}),
            (15, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (1.0, 0.0)}),
            (16, {'label': 'E', 'color': 'green', 'level': 2, 'pos': (0.85, 0.55)}),
            (17, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (0.5375, 0.8625)}),
            (18, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (1.0125, 0.7875)}),
            (19, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (1.3375, 0.2625)}),
            (20, {'label': 'I', 'color': 'orange', 'level': 2, 'pos': (0.5125, 0.2875)}),
        ])

        result_graph.add_edges_from([
            (0, 6),
            (6, 1), (6, 2), (6, 3), (6, 4),
            (2, 4), (4, 3), (3, 5), (5, 1),
            (1, 2),
            (6, 17), (6, 18), (6, 19), (6, 20),
            (8, 12), (8, 13), (13, 16), (13, 9),
            (9, 14), (14, 16), (14, 11), (11, 15),
            (15, 16), (15, 10), (10, 12), (12, 16),
            (17, 8), (17, 13), (17, 16), (17, 12),
            (18, 13), (18, 9), (18, 14), (18, 16),
            (19, 16), (19, 14), (19, 11), (19, 15),
            (20, 12), (20, 16), (20, 15), (20, 10),
            (6, 7),
        ]
        )
        graph.graph['max_id'] = 7
        graph.graph['max_level'] = 1

        left_side = generate_p3_left_side_graph()
        p3(graph, p3_p4_strategy(graph, left_side))

        self.assertEqual(len(graph.nodes()), 21)
        self.assertEqual(len(graph.edges()), 43)
        self.assertTrue(nx.is_isomorphic(graph, result_graph))

    def test_p3_production_with_p4_graph(self):
        graph = nx.Graph()
        graph.add_nodes_from(
            [(1, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.4, 1.2)}),
                              (2, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (1, 1)}),
                              (3, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0, 0)}),
                              (4, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (2, 0)}),
                              (5, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.2, 0.6)}),
                              (7, {'label': 'E', 'color': 'blue', 'level': 1, 'pos': (0.7, 1.1)}),
                              (6, {'label': 'I', 'color': 'brown', 'level': 1, 'pos': (0.85, 0.55)})
                              ]
        )

        graph.add_edges_from(
            [
                (0, 6),
                (6, 1), (6, 2), (6, 3), (6, 4),
                (2, 4), (4, 3), (3, 5), (5, 1),
                (1, 7), (7, 2)
            ]
        )

        graph.graph['max_id'] = 7
        graph.graph['max_level'] = 1

        left_side = generate_p3_left_side_graph()
        with self.assertRaises(IndexError):
            p3(graph, p3_p4_strategy(graph, left_side))


if __name__ == '__main__':
    unittest.main()

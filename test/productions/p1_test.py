import unittest
import networkx as nx
from productions.p1 import is_pos_valid, is_graph_valid, p1


class IsPosValidTest(unittest.TestCase):
    def test_right_pos(self):
        pos = {1: (0, 0), 2: (0, 0), 3: (0, 0), 4: (0, 0)}
        self.assertTrue(is_pos_valid(pos))

    def test_missing_key(self):
        pos = {1: (0, 0), 2: (0, 0), 4: (0, 0)}
        self.assertFalse(is_pos_valid(pos))

    def test_too_much_keys(self):
        pos = {1: (0, 0), 2: (0, 0), 3: (0, 0), 4: (0, 0), 5: (0, 0)}
        self.assertTrue(is_pos_valid(pos))

    def test_wrong_value_type(self):
        pos = {1: (0, 0), 2: 0, 3: (0, 0), 4: (0, 0)}
        self.assertFalse(is_pos_valid(pos))

    def test_wrong_value_length(self):
        pos = {1: (0, 0), 2: (0,), 3: (0, 0), 4: (0, 0)}
        self.assertFalse(is_pos_valid(pos))


class IsGraphValidTest(unittest.TestCase):
    def test_right_graph(self):
        graph = nx.Graph()
        graph.add_node(0, label='S')
        self.assertTrue(is_graph_valid(graph))

    def test_too_much_nodes(self):
        graph = nx.Graph()
        graph.add_node(0, label='S')
        graph.add_node(11, label='S')
        self.assertFalse(is_graph_valid(graph))

    def test_first_node_id_is_not_zero(self):
        graph = nx.Graph()
        graph.add_node(4, label='S')
        self.assertFalse(is_graph_valid(graph))

    def test_first_node_without_label(self):
        graph = nx.Graph()
        graph.add_node(0)
        self.assertFalse(is_graph_valid(graph))

    def test_first_node_with_wrong_label(self):
        graph = nx.Graph()
        graph.add_node(0, label='q')
        self.assertFalse(is_graph_valid(graph))


def initialize_graph():
    graph = nx.Graph(max_id=0, max_level=0)
    graph.add_node(0, label='S', color="red", level=0, pos=(0.5, 1.5))
    return graph


class P1Test(unittest.TestCase):
    def setUp(self):
        self.graph = initialize_graph()
        self.pos = {1: (0, 1), 2: (1, 1), 3: (0, 0), 4: (1, 0)}

    def test_p1_graph_attributes(self):
        p1(self.graph, self.pos)

        self.assertTrue('max_id' in self.graph.graph)
        self.assertTrue('max_level' in self.graph.graph)
        self.assertEqual(self.graph.graph['max_id'], 5)
        self.assertEqual(self.graph.graph['max_level'], 1)

    def test_p1_graph_nodes(self):
        p1(self.graph, self.pos)

        self.assertEqual(list(self.graph.nodes), [0, 1, 2, 3, 4, 5])
        self.assertEqual(self.graph.nodes[0]['label'], 'e')
        self.assertEqual(self.graph.nodes[5]['label'], 'I')
        self.assertEqual(self.graph.nodes[5]['level'], 1)
        for i in [1, 2, 3, 4]:
            self.assertDictEqual(self.graph.nodes[i], {"label": 'E', "color": "blue", "level": 1, "pos": self.pos[i]})

    def test_p1_graph_edges(self):
        p1(self.graph, self.pos)

        expected_edges_sets = [{0, 5},
                               {5, 1}, {5, 2}, {5, 3}, {5, 4},
                               {1, 2}, {2, 4}, {4, 3}, {3, 1}]
        self.assertEqual(len(self.graph.edges), len(expected_edges_sets))
        for edge in self.graph.edges:
            self.assertIn(set(edge), expected_edges_sets)


if __name__ == '__main__':
    unittest.main()

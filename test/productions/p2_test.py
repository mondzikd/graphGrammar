import unittest

import networkx as nx

from productions.p1 import p1
from productions.p2 import is_input_valid, generate_p2_left_side_graph
from strategies.super_simple_strategy import super_simple_strategy
from utils.initialize import initialize


class GenerateP2LeftSideGraphTest(unittest.TestCase):
    pass


class IsInputValidTest(unittest.TestCase):
    def test_none(self):
        graph = nx.Graph()
        self.assertFalse(is_input_valid(None, None))
        self.assertFalse(is_input_valid(graph, None))
        self.assertFalse(is_input_valid(None, []))

    def test_mapping_keys(self):
        graph = initialize()
        p1(graph)
        left_side = generate_p2_left_side_graph()
        mapping = super_simple_strategy(graph, left_side)

        self.assertFalse(is_input_valid(graph, mapping))
        # {'_UPPER_LEFT_ID': 1, '_UPPER_RIGHT_ID': 2, '_LOWER_LEFT_ID': 3, '_LOWER_RIGHT_ID': 4, '_CENTER_ID': 5}


if __name__ == '__main__':
    unittest.main()

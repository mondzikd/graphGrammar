import unittest
import networkx as nx

from productions.p8 import p8


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # given
        graph = nx.Graph(max_id=0, max_level=0)
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
        ])
        graph.add_edges_from([
            (1, 2), (1, 4), (1, 6), (1, 8),
            (2, 3), (2, 6), (2, 7),
            (3, 7),
            (4, 5), (4, 8), (4, 9),
            (5, 9)
        ])

        
        
        #deepest_nodes = list(filter(lambda x: x[1]['level'] == 3, graph.nodes(data=True)))
        max_level = max(map(lambda x: x[1]['level'], graph.nodes(data=True)))
        deepest_nodes = (filter(lambda x: x[1]['level'] == max_level, graph.nodes(data=True)))


        

        result_graph = nx.Graph(max_id=0, max_level=0)
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
        nx.is_isomorphic(graph, result_graph)


if __name__ == '__main__':
    unittest.main()

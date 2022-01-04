import networkx as nx

_UPPER_LEFT_ID = 0
_UPPER_RIGHT_ID = 1
_LOWER_RIGHT_ID = 2
_LOWER_LEFT_ID = 3
_CENTER_ID = 4
_LEFT_MIDDLE_ID = 5
_UPPER_MIDDLE_ID = 6
_RIGHT_MIDDLE_ID = 7



def generate_p7_left_side_graph():
    graph = nx.Graph(id="left_p7")

    graph.add_nodes_from([
        (_UPPER_LEFT_ID, {"label": "E"}),
        (_UPPER_RIGHT_ID, {"label": "E"}),
        (_LOWER_LEFT_ID, {"label": "E"}),
        (_LOWER_RIGHT_ID, {"label": "E"}),
        (_LEFT_MIDDLE_ID, {"label": "E"}),
        (_UPPER_MIDDLE_ID, {"label": "E"}),
        (_RIGHT_MIDDLE_ID, {"label": "E"}),
        (_CENTER_ID, {"label": "I"})
    ])

    graph.add_edges_from([
        (_UPPER_LEFT_ID, _UPPER_MIDDLE_ID), (_UPPER_MIDDLE_ID, _UPPER_RIGHT_ID), (_UPPER_RIGHT_ID, _RIGHT_MIDDLE_ID),
        (_RIGHT_MIDDLE_ID, _LOWER_RIGHT_ID), (_LOWER_RIGHT_ID, _LOWER_LEFT_ID), (_LOWER_LEFT_ID, _LEFT_MIDDLE_ID), (_LEFT_MIDDLE_ID, _UPPER_LEFT_ID),
        (_CENTER_ID, _UPPER_LEFT_ID), (_CENTER_ID, _UPPER_RIGHT_ID), (_CENTER_ID, _LOWER_RIGHT_ID), (_CENTER_ID, _LOWER_LEFT_ID)
    ])

    return graph

def generate_p7_left_side_graph_test():
    graph = nx.Graph(id="left_p7")

    graph.add_nodes_from([
        (_UPPER_LEFT_ID, {"label": "E", "color": "blue", "level": 1, "pos": (1, 3)}),
        (_UPPER_RIGHT_ID, {"label": "E", "color": "blue", "level": 1, "pos": (3, 3)}),
        (_LOWER_LEFT_ID, {"label": "E", "color": "blue", "level": 1, "pos": (1, 1)}),
        (_LOWER_RIGHT_ID, {"label": "E", "color": "blue", "level": 1, "pos": (3, 1)}),
        (_LEFT_MIDDLE_ID, {"label": "E", "color": "blue", "level": 1, "pos": (1, 2)}),
        (_UPPER_MIDDLE_ID, {"label": "E", "color": "blue", "level": 1, "pos": (2, 3)}),
        (_RIGHT_MIDDLE_ID, {"label": "E", "color": "blue", "level": 1, "pos": (3, 2)}),
        (_CENTER_ID, {"label": "I", "color": "brown", "level": 1, "pos": (2, 2)})
    ])

    graph.add_edges_from([
        (_UPPER_LEFT_ID, _UPPER_MIDDLE_ID), (_UPPER_MIDDLE_ID, _UPPER_RIGHT_ID), (_UPPER_RIGHT_ID, _RIGHT_MIDDLE_ID),
        (_RIGHT_MIDDLE_ID, _LOWER_RIGHT_ID), (_LOWER_RIGHT_ID, _LOWER_LEFT_ID), (_LOWER_LEFT_ID, _LEFT_MIDDLE_ID), (_LEFT_MIDDLE_ID, _UPPER_LEFT_ID),
        (_CENTER_ID, _UPPER_LEFT_ID), (_CENTER_ID, _UPPER_RIGHT_ID), (_CENTER_ID, _LOWER_RIGHT_ID), (_CENTER_ID, _LOWER_LEFT_ID)
    ])

    return graph

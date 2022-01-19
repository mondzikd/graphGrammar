import networkx as nx

_OLD_E_ID = 0
_OLD_LEFT_I_ID = 1
_OLD_RIGHT_I_ID = 2
_UPPER_LEFT_I_ID = 3
_UPPER_RIGHT_I_ID = 4
_LOWER_RIGHT_I_ID = 5
_LOWER_LEFT_I_ID = 6
_UPPER_LEFT_E_ID = 7
_UPPER_RIGHT_E_ID = 8
_MIDDLE_LEFT_E_ID = 9
_MIDDLE_RIGHT_E_ID = 10
_LOWER_LEFT_E_ID = 11
_LOWER_RIGHT_E_ID = 12




def generate_p7_left_side_graph():
    graph = nx.Graph(id="left_p7")

    graph.add_nodes_from([
        (_OLD_E_ID, {"label": "E"}),
        (_OLD_LEFT_I_ID, {"label": "i"}),
        (_OLD_RIGHT_I_ID, {"label": "i"}),
        (_UPPER_LEFT_I_ID, {"label": "I"}),
        (_UPPER_RIGHT_I_ID, {"label": "I"}),
        (_LOWER_RIGHT_I_ID, {"label": "I"}),
        (_LOWER_LEFT_I_ID, {"label": "I"}),
        (_UPPER_LEFT_E_ID, {"label": "E"}),
        (_UPPER_RIGHT_E_ID, {"label": "E"}),
        (_MIDDLE_LEFT_E_ID, {"label": "E"}),
        (_MIDDLE_RIGHT_E_ID, {"label": "E"}),
        (_LOWER_LEFT_E_ID, {"label": "E"}),
        (_LOWER_RIGHT_E_ID, {"label": "E"}),
    ])

    graph.add_edges_from([
        (_OLD_E_ID, _OLD_LEFT_I_ID), (_OLD_E_ID, _OLD_RIGHT_I_ID), (_OLD_LEFT_I_ID, _UPPER_LEFT_I_ID), (_OLD_LEFT_I_ID, _LOWER_LEFT_I_ID),
        (_OLD_RIGHT_I_ID, _UPPER_RIGHT_I_ID), (_OLD_RIGHT_I_ID, _LOWER_RIGHT_I_ID), (_UPPER_LEFT_I_ID, _UPPER_LEFT_E_ID), (_UPPER_LEFT_I_ID, _MIDDLE_LEFT_E_ID),
        (_LOWER_LEFT_I_ID, _MIDDLE_LEFT_E_ID), (_LOWER_LEFT_I_ID, _LOWER_LEFT_E_ID), (_UPPER_RIGHT_I_ID, _UPPER_RIGHT_E_ID), (_UPPER_RIGHT_I_ID, _MIDDLE_RIGHT_E_ID),
        (_LOWER_RIGHT_I_ID, _MIDDLE_RIGHT_E_ID), (_LOWER_RIGHT_I_ID, _LOWER_RIGHT_E_ID), (_UPPER_LEFT_E_ID, _MIDDLE_LEFT_E_ID), (_MIDDLE_LEFT_E_ID, _LOWER_LEFT_E_ID),
        (_UPPER_RIGHT_E_ID, _MIDDLE_RIGHT_E_ID), (_MIDDLE_RIGHT_E_ID, _LOWER_RIGHT_E_ID)
    ])

    return graph


def p7(graph, mapping):
    """ P7 production

    Parameters:
        graph (nx.Graph): graph on which production will be applied.

        mapping (dict):
            keys are ids of template production left side graph (from generate_p7_left_side_graph()),
            values are corresponding ids from graph, where we need to apply production

    Returns:
        Nothing. applies production on argument graph in place or raises an error if input not valid.
    """
    if not is_input_valid(graph, mapping):
        raise Exception("Expected right input")

    curr_lower_level = graph.nodes[mapping[_LOWER_LEFT_E_ID]]['level'] + 1
    curr_middle_level = graph.nodes[mapping[_MIDDLE_LEFT_E_ID]]['level'] + 1
    curr_upper_level = graph.nodes[mapping[_UPPER_LEFT_E_ID]]['level'] + 1

    graph.graph['max_level'] = max(curr_lower_level, curr_middle_level, curr_upper_level, graph.graph['max_level'])

    graph.remove_nodes_from([mapping[_LOWER_RIGHT_E_ID], mapping[_MIDDLE_RIGHT_E_ID], mapping[_UPPER_RIGHT_E_ID]])
    graph.add_edges_from([
        (mapping[_UPPER_LEFT_E_ID], mapping[_UPPER_RIGHT_I_ID]), (mapping[_MIDDLE_LEFT_E_ID], mapping[_UPPER_RIGHT_I_ID]), (mapping[_MIDDLE_LEFT_E_ID], mapping[_LOWER_RIGHT_I_ID]), (mapping[_LOWER_LEFT_E_ID], mapping[_LOWER_RIGHT_I_ID])
    ])

def generate_p7_left_side_graph_test():
    graph = nx.Graph(id="left_p7")

    graph.graph["max_level"] = 3

    graph.add_nodes_from([
        (_OLD_E_ID, {"label": "E", "level": 1, "color": "green", "pos": (10, 10)}),
        (_OLD_LEFT_I_ID, {"label": "i", "level": 2, "color": "brown", "pos": (9, 9)}),
        (_OLD_RIGHT_I_ID, {"label": "i", "level": 2, "color": "brown", "pos": (11, 9)}),
        (_UPPER_LEFT_I_ID, {"label": "I", "level": 3, "color": "grey", "pos": (8, 6)}),
        (_UPPER_RIGHT_I_ID, {"label": "I", "level": 3, "color": "grey", "pos": (12, 6)}),
        (_LOWER_RIGHT_I_ID, {"label": "I", "level": 3, "color": "grey", "pos": (12, 4)}),
        (_LOWER_LEFT_I_ID, {"label": "I", "level": 3, "color": "grey", "pos": (8, 4)}),
        (_UPPER_LEFT_E_ID, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
        (_UPPER_RIGHT_E_ID, {"label": "E", "level": 3, "color": "blue", "pos": (10, 7)}),
        (_MIDDLE_LEFT_E_ID, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
        (_MIDDLE_RIGHT_E_ID, {"label": "E", "level": 3, "color": "blue", "pos": (10, 5)}),
        (_LOWER_LEFT_E_ID, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)}),
        (_LOWER_RIGHT_E_ID, {"label": "E", "level": 3, "color": "blue", "pos": (10, 3)})
    ])

    graph.add_edges_from([
        (_OLD_E_ID, _OLD_LEFT_I_ID), (_OLD_E_ID, _OLD_RIGHT_I_ID), (_OLD_LEFT_I_ID, _UPPER_LEFT_I_ID), (_OLD_LEFT_I_ID, _LOWER_LEFT_I_ID),
        (_OLD_RIGHT_I_ID, _UPPER_RIGHT_I_ID), (_OLD_RIGHT_I_ID, _LOWER_RIGHT_I_ID), (_UPPER_LEFT_I_ID, _UPPER_LEFT_E_ID), (_UPPER_LEFT_I_ID, _MIDDLE_LEFT_E_ID),
        (_LOWER_LEFT_I_ID, _MIDDLE_LEFT_E_ID), (_LOWER_LEFT_I_ID, _LOWER_LEFT_E_ID), (_UPPER_RIGHT_I_ID, _UPPER_RIGHT_E_ID), (_UPPER_RIGHT_I_ID, _MIDDLE_RIGHT_E_ID),
        (_LOWER_RIGHT_I_ID, _MIDDLE_RIGHT_E_ID), (_LOWER_RIGHT_I_ID, _LOWER_RIGHT_E_ID), (_UPPER_LEFT_E_ID, _MIDDLE_LEFT_E_ID), (_MIDDLE_LEFT_E_ID, _LOWER_LEFT_E_ID),
        (_UPPER_RIGHT_E_ID, _MIDDLE_RIGHT_E_ID), (_MIDDLE_RIGHT_E_ID, _LOWER_RIGHT_E_ID)
    ])

    return graph

def is_input_valid(graph, mapping):
    return graph.nodes[mapping[_MIDDLE_RIGHT_E_ID]]["pos"] == graph.nodes[mapping[_MIDDLE_LEFT_E_ID]]["pos"] and graph.nodes[mapping[_UPPER_RIGHT_E_ID]]["pos"] == graph.nodes[mapping[_UPPER_LEFT_E_ID]]["pos"] \
           and graph.nodes[mapping[_LOWER_LEFT_E_ID]]["pos"] == graph.nodes[mapping[_LOWER_RIGHT_E_ID]]["pos"] and is_middle_E_in_center(graph, mapping)

def is_middle_E_in_center(graph, mapping):
    return (graph.nodes[mapping[_LOWER_LEFT_E_ID]]["pos"] + graph.nodes[mapping[_UPPER_LEFT_E_ID]]["pos"])/2 == graph.nodes[mapping[_MIDDLE_LEFT_E_ID]]["pos"]
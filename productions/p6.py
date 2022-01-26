import networkx as nx

from utils.calculate_position import calculate_I_pos, calculate_avg

_UPPER_LEFT_ID = 1
_UPPER_MIDDLE_ID = 2
_UPPER_RIGHT_ID = 3
_MIDDLE_RIGHT_ID = 4
_LOWER_RIGHT_ID = 5
_LOWER_MIDDLE_ID = 6
_LOWER_LEFT_ID = 7
_MIDDLE_LEFT_ID = 8
_CENTER_ID = 9


def generate_p6_left_side_graph():
    """ Generates template p6 production left side graph

        Returns:
            nx.Graph which should be used in finding subgraph strategy.
        """
    graph = nx.Graph(id="left_p6")

    graph.add_nodes_from([
        (_UPPER_LEFT_ID, {"label": "E"}),
        (_UPPER_MIDDLE_ID, {"label": "E"}),
        (_UPPER_RIGHT_ID, {"label": "E"}),
        (_MIDDLE_RIGHT_ID, {"label": "E"}),
        (_LOWER_RIGHT_ID, {"label": "E"}),
        (_LOWER_MIDDLE_ID, {"label": "E"}),
        (_LOWER_LEFT_ID, {"label": "E"}),
        (_MIDDLE_LEFT_ID, {"label": "E"}),
        (_CENTER_ID, {"label": "I"})
    ])

    graph.add_edges_from([
        (_CENTER_ID, _UPPER_LEFT_ID), (_CENTER_ID, _UPPER_RIGHT_ID),
        (_CENTER_ID, _LOWER_LEFT_ID), (_CENTER_ID, _LOWER_RIGHT_ID),
        (_UPPER_LEFT_ID, _UPPER_MIDDLE_ID), (_UPPER_MIDDLE_ID, _UPPER_RIGHT_ID),
        (_UPPER_RIGHT_ID, _MIDDLE_RIGHT_ID), (_MIDDLE_RIGHT_ID, _LOWER_RIGHT_ID),
        (_LOWER_RIGHT_ID, _LOWER_MIDDLE_ID), (_LOWER_MIDDLE_ID,_LOWER_LEFT_ID),
        (_LOWER_LEFT_ID, _MIDDLE_LEFT_ID), (_MIDDLE_LEFT_ID, _UPPER_LEFT_ID),
    ])

    return graph


def p6(graph, mapping):
    """ P6 production

    Parameters:
        graph (nx.Graph): graph on which production will be applied.

        mapping (dict):
            keys are ids of template production left side graph (from generate_p5_left_side_graph()),
            values are corresponding ids from graph, where we need to apply production

    Returns:
        Nothing. applies production on argument graph in place or raises an error if input not valid.
    """
    if not is_input_valid(graph, mapping):
        raise Exception("Expected right input")

    max_id = graph.graph["max_id"]
    curr_level = graph.nodes[mapping[_CENTER_ID]]['level'] + 1

    graph.graph["max_id"] = max_id + 15
    graph.graph['max_level'] = max(curr_level, graph.graph['max_level'])

    graph.nodes[mapping[_CENTER_ID]]['label'] = 'i'
    graph.nodes[mapping[_CENTER_ID]]['color'] = "brown"

    graph.add_nodes_from([
        (max_id + 1,
         {"label": "E", "color": "green", "level": curr_level, "pos": graph.nodes[mapping[_UPPER_LEFT_ID]]["pos"]}),
        (max_id + 2,
         {"label": "E", "color": "green", "level": curr_level, "pos": graph.nodes[mapping[_UPPER_RIGHT_ID]]["pos"]}),
        (max_id + 3,
         {"label": "E", "color": "green", "level": curr_level, "pos": graph.nodes[mapping[_LOWER_LEFT_ID]]["pos"]}),
        (max_id + 4,
         {"label": "E", "color": "green", "level": curr_level, "pos": graph.nodes[mapping[_LOWER_RIGHT_ID]]["pos"]}),

        (max_id + 5, {"label": "E", "color": "green", "level": curr_level,
                      "pos": calculate_avg(graph.nodes[mapping[_UPPER_LEFT_ID]]["pos"],
                                           graph.nodes[mapping[_UPPER_RIGHT_ID]]["pos"])}),
        (max_id + 6, {"label": "E", "color": "green", "level": curr_level,
                      "pos": calculate_avg(graph.nodes[mapping[_UPPER_RIGHT_ID]]["pos"],
                                           graph.nodes[mapping[_LOWER_RIGHT_ID]]["pos"])}),
        (max_id + 7, {"label": "E", "color": "green", "level": curr_level,
                      "pos": calculate_avg(graph.nodes[mapping[_LOWER_LEFT_ID]]["pos"],
                                           graph.nodes[mapping[_LOWER_RIGHT_ID]]["pos"])}),
        (max_id + 8, {"label": "E", "color": "green", "level": curr_level,
                      "pos": calculate_avg(graph.nodes[mapping[_LOWER_LEFT_ID]]["pos"],
                                           graph.nodes[mapping[_UPPER_LEFT_ID]]["pos"])}),
        (max_id + 9, {"label": "E", "color": "green", "level": curr_level,
                      "pos": calculate_avg(graph.nodes[mapping[_UPPER_LEFT_ID]]["pos"],
                                           graph.nodes[mapping[_LOWER_RIGHT_ID]]["pos"])}),
    ])

    graph.add_nodes_from([
        (max_id + 10, {"label": "I", "color": "orange", "level": curr_level,
                       "pos": calculate_I_pos(graph.nodes[max_id + 1]["pos"], graph.nodes[max_id + 5]["pos"],
                                              graph.nodes[max_id + 8]["pos"], graph.nodes[max_id + 9]["pos"])}),
        (max_id + 11, {"label": "I", "color": "orange", "level": curr_level,
                       "pos": calculate_I_pos(graph.nodes[max_id + 5]["pos"], graph.nodes[max_id + 2]["pos"],
                                              graph.nodes[max_id + 9]["pos"], graph.nodes[max_id + 6]["pos"])}),
        (max_id + 12, {"label": "I", "color": "orange", "level": curr_level,
                       "pos": calculate_I_pos(graph.nodes[max_id + 8]["pos"], graph.nodes[max_id + 9]["pos"],
                                              graph.nodes[max_id + 3]["pos"], graph.nodes[max_id + 7]["pos"])}),
        (max_id + 13, {"label": "I", "color": "orange", "level": curr_level,
                       "pos": calculate_I_pos(graph.nodes[max_id + 9]["pos"], graph.nodes[max_id + 6]["pos"],
                                              graph.nodes[max_id + 7]["pos"], graph.nodes[max_id + 4]["pos"])}),
    ])

    graph.add_edges_from([
        (mapping[_CENTER_ID], max_id + 10), (mapping[_CENTER_ID], max_id + 11), (mapping[_CENTER_ID], max_id + 12),
        (mapping[_CENTER_ID], max_id + 13),
        (max_id + 1, max_id + 5), (max_id + 1, max_id + 8), (max_id + 9, max_id + 5), (max_id + 9, max_id + 8),
        (max_id + 5, max_id + 2), (max_id + 2, max_id + 6), (max_id + 6, max_id + 9),
        (max_id + 8, max_id + 3), (max_id + 3, max_id + 7), (max_id + 7, max_id + 9),
        (max_id + 7, max_id + 4), (max_id + 4, max_id + 6),

        (max_id + 10, max_id + 1), (max_id + 10, max_id + 5), (max_id + 10, max_id + 8), (max_id + 10, max_id + 9),
        (max_id + 11, max_id + 5), (max_id + 11, max_id + 2), (max_id + 11, max_id + 9), (max_id + 11, max_id + 6),
        (max_id + 12, max_id + 8), (max_id + 12, max_id + 9), (max_id + 12, max_id + 3), (max_id + 12, max_id + 7),
        (max_id + 13, max_id + 9), (max_id + 13, max_id + 6), (max_id + 13, max_id + 7), (max_id + 13, max_id + 4)
    ])


def generate_p6_test_correct():
    graph = nx.Graph(id="left_p5")

    graph.graph["max_level"] = 2
    graph.graph['max_id'] = 9

    graph.add_nodes_from([
        (_UPPER_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 12)}),
        (_UPPER_MIDDLE_ID, {"label": "E", "level": 2, "color": "blue", "pos": (6, 12)}),
        (_UPPER_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 12)}),
        (_MIDDLE_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 6)}),
        (_LOWER_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 0)}),
        (_LOWER_MIDDLE_ID, {"label": "E", "level": 2, "color": "blue", "pos": (6, 0)}),
        (_LOWER_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 0)}),
        (_MIDDLE_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 6)}),
        (_CENTER_ID, {"label": "I", "level": 2, "color": "red", "pos": (6, 6)})
        ])

    graph.add_edges_from([
        (_CENTER_ID, _UPPER_LEFT_ID), (_CENTER_ID, _UPPER_RIGHT_ID),
        (_CENTER_ID, _LOWER_LEFT_ID), (_CENTER_ID, _LOWER_RIGHT_ID),
        (_UPPER_LEFT_ID, _UPPER_MIDDLE_ID), (_UPPER_MIDDLE_ID, _UPPER_RIGHT_ID),
        (_UPPER_RIGHT_ID, _MIDDLE_RIGHT_ID), (_MIDDLE_RIGHT_ID, _LOWER_RIGHT_ID),
        (_LOWER_RIGHT_ID, _LOWER_MIDDLE_ID), (_LOWER_MIDDLE_ID,_LOWER_LEFT_ID),
        (_LOWER_LEFT_ID, _MIDDLE_LEFT_ID), (_MIDDLE_LEFT_ID, _UPPER_LEFT_ID),
    ])

    return graph


def generate_p6_test_incorrect_position():
    graph = nx.Graph(id="left_p5")

    graph.graph["max_level"] = 2
    graph.graph['max_id'] = 9

    graph.add_nodes_from([
        (_UPPER_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 12)}),
        (_UPPER_MIDDLE_ID, {"label": "I", "level": 2, "color": "blue", "pos": (6, 12)}),
        (_UPPER_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 12)}),
        (_MIDDLE_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (11, 6)}),
        (_LOWER_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 0)}),
        (_LOWER_MIDDLE_ID, {"label": "E", "level": 2, "color": "blue", "pos": (6, 0)}),
        (_LOWER_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 0)}),
        (_MIDDLE_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 3)}),
        (_CENTER_ID, {"label": "I", "level": 2, "color": "red", "pos": (6, 6)})
        ])

    graph.add_edges_from([
        (_CENTER_ID, _UPPER_LEFT_ID), (_CENTER_ID, _UPPER_RIGHT_ID),
        (_CENTER_ID, _LOWER_LEFT_ID), (_CENTER_ID, _LOWER_RIGHT_ID),
        (_UPPER_LEFT_ID, _UPPER_MIDDLE_ID), (_UPPER_MIDDLE_ID, _UPPER_RIGHT_ID),
        (_UPPER_RIGHT_ID, _MIDDLE_RIGHT_ID), (_MIDDLE_RIGHT_ID, _LOWER_RIGHT_ID),
        (_LOWER_RIGHT_ID, _LOWER_MIDDLE_ID), (_LOWER_MIDDLE_ID,_LOWER_LEFT_ID),
        (_LOWER_LEFT_ID, _MIDDLE_LEFT_ID), (_MIDDLE_LEFT_ID, _UPPER_LEFT_ID),
    ])

    return graph


def generate_p6_test_incorrect_labels():
    graph = nx.Graph(id="left_p5")

    graph.graph["max_level"] = 2
    graph.graph['max_id'] = 9

    graph.add_nodes_from([
        (_UPPER_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 12)}),
        (_UPPER_MIDDLE_ID, {"label": "I", "level": 2, "color": "green", "pos": (6, 12)}),
        (_UPPER_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 12)}),
        (_MIDDLE_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 6)}),
        (_LOWER_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 0)}),
        (_LOWER_MIDDLE_ID, {"label": "E", "level": 2, "color": "blue", "pos": (6, 0)}),
        (_LOWER_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 0)}),
        (_MIDDLE_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 6)}),
        (_CENTER_ID, {"label": "I", "level": 2, "color": "red", "pos": (6, 6)})
        ])

    graph.add_edges_from([
        (_CENTER_ID, _UPPER_LEFT_ID), (_CENTER_ID, _UPPER_RIGHT_ID),
        (_CENTER_ID, _LOWER_LEFT_ID), (_CENTER_ID, _LOWER_RIGHT_ID),
        (_UPPER_LEFT_ID, _UPPER_MIDDLE_ID), (_UPPER_MIDDLE_ID, _UPPER_RIGHT_ID),
        (_UPPER_RIGHT_ID, _MIDDLE_RIGHT_ID), (_MIDDLE_RIGHT_ID, _LOWER_RIGHT_ID),
        (_LOWER_RIGHT_ID, _LOWER_MIDDLE_ID), (_LOWER_MIDDLE_ID,_LOWER_LEFT_ID),
        (_LOWER_LEFT_ID, _MIDDLE_LEFT_ID), (_MIDDLE_LEFT_ID, _UPPER_LEFT_ID),
    ])

    return graph


def generate_p6_test_missing_vertex():
    graph = nx.Graph(id="left_p5")

    graph.graph["max_level"] = 2
    graph.graph['max_id'] = 9

    graph.add_nodes_from([
        (_UPPER_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 12)}),
        (_UPPER_MIDDLE_ID, {"label": "E", "level": 2, "color": "blue", "pos": (6, 12)}),
        (_UPPER_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 12)}),
        (_LOWER_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 0)}),
        (_LOWER_MIDDLE_ID, {"label": "E", "level": 2, "color": "blue", "pos": (6, 0)}),
        (_LOWER_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 0)}),
        (_MIDDLE_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 6)}),
        (_CENTER_ID, {"label": "I", "level": 2, "color": "red", "pos": (6, 6)})
        ])

    graph.add_edges_from([
        (_CENTER_ID, _UPPER_LEFT_ID), (_CENTER_ID, _UPPER_RIGHT_ID),
        (_CENTER_ID, _LOWER_LEFT_ID), (_CENTER_ID, _LOWER_RIGHT_ID),
        (_UPPER_LEFT_ID, _UPPER_MIDDLE_ID), (_UPPER_MIDDLE_ID, _UPPER_RIGHT_ID),
        (_UPPER_RIGHT_ID, _LOWER_RIGHT_ID),
        (_LOWER_RIGHT_ID, _LOWER_MIDDLE_ID), (_LOWER_MIDDLE_ID,_LOWER_LEFT_ID),
        (_LOWER_LEFT_ID, _MIDDLE_LEFT_ID), (_MIDDLE_LEFT_ID, _UPPER_LEFT_ID),
    ])

    return graph


def generate_p6_test_missing_edge():
    graph = nx.Graph(id="left_p5")

    graph.graph["max_level"] = 2
    graph.graph['max_id'] = 9

    graph.add_nodes_from([
        (_UPPER_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 12)}),
        (_UPPER_MIDDLE_ID, {"label": "E", "level": 2, "color": "blue", "pos": (6, 12)}),
        (_UPPER_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 12)}),
        (_MIDDLE_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 6)}),
        (_LOWER_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 0)}),
        (_LOWER_MIDDLE_ID, {"label": "E", "level": 2, "color": "blue", "pos": (6, 0)}),
        (_LOWER_RIGHT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (12, 0)}),
        (_MIDDLE_LEFT_ID, {"label": "E", "level": 2, "color": "blue", "pos": (0, 6)}),
        (_CENTER_ID, {"label": "I", "level": 2, "color": "red", "pos": (6, 6)})
        ])

    graph.add_edges_from([
        (_CENTER_ID, _UPPER_LEFT_ID),
        (_CENTER_ID, _LOWER_LEFT_ID), (_CENTER_ID, _LOWER_RIGHT_ID),
        (_UPPER_LEFT_ID, _UPPER_MIDDLE_ID), (_UPPER_MIDDLE_ID, _UPPER_RIGHT_ID),
        (_UPPER_RIGHT_ID, _MIDDLE_RIGHT_ID), (_MIDDLE_RIGHT_ID, _LOWER_RIGHT_ID),
        (_LOWER_RIGHT_ID, _LOWER_MIDDLE_ID), (_LOWER_MIDDLE_ID,_LOWER_LEFT_ID),
        (_LOWER_LEFT_ID, _MIDDLE_LEFT_ID), (_MIDDLE_LEFT_ID, _UPPER_LEFT_ID),
    ])

    return graph


def generate_bigger_p6_1_test():
    graph = nx.Graph(id="left_p6")

    graph.graph["max_level"] = 2
    graph.graph['max_id'] = 17

    graph.add_nodes_from([
        (1, {"label": "E", "level": 2, "color": "green", "pos": (0, 12)}),
        (2, {"label": "E", "level": 2, "color": "blue", "pos": (6, 12)}),
        (3, {"label": "E", "level": 2, "color": "blue", "pos": (9, 12)}),
        (4, {"label": "E", "level": 2, "color": "blue", "pos": (12, 12)}),
        (5, {"label": "E", "level": 2, "color": "blue", "pos": (12, 9)}),
        (6, {"label": "E", "level": 2, "color": "blue", "pos": (12, 6)}),
        (7, {"label": "E", "level": 2, "color": "green", "pos": (12, 0)}),
        (8, {"label": "E", "level": 2, "color": "green", "pos": (6, 0)}),
        (9, {"label": "E", "level": 2, "color": "green", "pos": (0, 0)}),
        (10, {"label": "E", "level": 2, "color": "green", "pos": (0, 6)}),
        (11, {"label": "E", "level": 2, "color": "blue", "pos": (6, 6)}),
        (12, {"label": "E", "level": 2, "color": "blue", "pos": (6, 9)}),
        (13, {"label": "E", "level": 2, "color": "blue", "pos": (9, 6)}),

        (14, {"label": "I", "level": 2, "color": "orange", "pos": (3, 9)}),
        (15, {"label": "I", "level": 2, "color": "red", "pos": (9, 9)}),
        (16, {"label": "I", "level": 2, "color": "orange", "pos": (3, 3)}),
        (17, {"label": "I", "level": 2, "color": "orange", "pos": (9, 3)}),
        ])

    graph.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1),
        (10, 11), (11, 13), (13, 6), (2, 12), (12, 11), (11, 8),
        (1, 14), (2, 14), (10, 14), (11, 14),
        (2, 15), (4, 15), (6, 15), (11, 15),
        (8, 16), (9, 16), (10, 16), (11, 16),
        (6, 17), (7, 17), (8, 17), (11, 17)
    ])

    return graph


def generate_bigger_p6_2_test():
    graph = nx.Graph(id="left_p6")

    graph.graph["max_level"] = 2
    graph.graph['max_id'] = 21

    graph.add_nodes_from([
        (1, {"label": "E", "level": 2, "color": "blue", "pos": (0, 12)}),
        (2, {"label": "E", "level": 2, "color": "blue", "pos": (3, 12)}),
        (3, {"label": "E", "level": 2, "color": "blue", "pos": (6, 12)}),
        (4, {"label": "E", "level": 2, "color": "green", "pos": (12, 12)}),

        (5, {"label": "E", "level": 2, "color": "blue", "pos": (12, 6)}),
        (6, {"label": "E", "level": 2, "color": "blue", "pos": (12, 3)}),
        (7, {"label": "E", "level": 2, "color": "blue", "pos": (12, 0)}),

        (8, {"label": "E", "level": 2, "color": "blue", "pos": (9, 0)}),
        (9, {"label": "E", "level": 2, "color": "blue", "pos": (6, 0)}),
        (10, {"label": "E", "level": 2, "color": "green", "pos": (0, 0)}),

        (11, {"label": "E", "level": 2, "color": "blue", "pos": (0, 6)}),
        (12, {"label": "E", "level": 2, "color": "blue", "pos": (0, 9)}),

        (13, {"label": "E", "level": 2, "color": "blue", "pos": (6, 6)}),
        (14, {"label": "E", "level": 2, "color": "blue", "pos": (6, 9)}),
        (15, {"label": "E", "level": 2, "color": "blue", "pos": (9, 6)}),
        (16, {"label": "E", "level": 2, "color": "blue", "pos": (6, 3)}),
        (17, {"label": "E", "level": 2, "color": "blue", "pos": (3, 6)}),

        (18, {"label": "I", "level": 2, "color": "red", "pos": (3, 9)}),
        (19, {"label": "I", "level": 2, "color": "orange", "pos": (9, 9)}),
        (20, {"label": "I", "level": 2, "color": "orange", "pos": (3, 3)}),
        (21, {"label": "I", "level": 2, "color": "red", "pos": (9, 3)}),
        ])

    graph.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1),
        (10, 11), (11, 12), (12, 1),
        (11, 17), (17, 13), (13, 15), (15, 5), (3, 14), (14, 13), (13, 16), (16, 9),
        (1, 18), (3, 18), (13, 18), (11, 18),
        (3, 19), (4, 19), (5, 19), (13, 19),
        (11, 20), (13, 20), (9, 20), (10, 20),
        (13, 21), (5, 21), (7, 21), (9, 21)
    ])

    return graph


def is_input_valid(graph, mapping):
    is_valid = True
    for node_id in mapping:
        neighbors = [n for n in graph.neighbors(node_id)]
        if len(neighbors) != 2:
            continue
        neighbor_1_pos = graph.nodes[neighbors[0]]["pos"]
        neighbor_2_pos = graph.nodes[neighbors[1]]["pos"]

        middle_pos = calculate_avg(neighbor_1_pos, neighbor_2_pos)
        if middle_pos[0] != graph.nodes[node_id]["pos"][0] or middle_pos[1] != graph.nodes[node_id]["pos"][1]:
            is_valid = False

    print("Is valid? -> ", is_valid)
    return is_valid


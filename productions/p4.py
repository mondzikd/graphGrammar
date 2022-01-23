import networkx as nx

from utils.calculate_position import calculate_I_pos, calculate_avg

_UPPER_LEFT_ID = 121
_UPPER_RIGHT_ID = 137
_LOWER_RIGHT_ID = 1015
_LOWER_LEFT_ID = 1010
_CENTER_LEFT_ID = 1020
_UPPER_CENTER_ID = 1032
_CENTER_ID = 1026


def generate_p4_left_side_graph():
    """ Generates template p4 production left side graph

        Returns:
            nx.Graph which should be used in finding subgraph strategy.
        """
    graph = nx.Graph(id="left_p29")

    graph.add_nodes_from([
        (_UPPER_LEFT_ID, {"label": "E", "should_equidistant": False}),
        (_UPPER_RIGHT_ID, {"label": "E", "should_equidistant": False}),
        (_LOWER_LEFT_ID, {"label": "E", "should_equidistant": False}),
        (_LOWER_RIGHT_ID, {"label": "E", "should_equidistant": False}),
        (_CENTER_LEFT_ID, {"label": "E", "should_equidistant": True}),
        (_UPPER_CENTER_ID, {"label": "E", "should_equidistant": True}),
        (_CENTER_ID, {"label": "I", "should_equidistant": False})
    ])

    graph.add_edges_from([
        (_CENTER_ID, _UPPER_LEFT_ID), (_CENTER_ID, _UPPER_RIGHT_ID),
        (_CENTER_ID, _LOWER_LEFT_ID), (_CENTER_ID, _LOWER_RIGHT_ID),
        (_UPPER_LEFT_ID, _UPPER_CENTER_ID), (_UPPER_RIGHT_ID, _LOWER_RIGHT_ID),
        (_LOWER_RIGHT_ID, _LOWER_LEFT_ID), (_LOWER_LEFT_ID, _CENTER_LEFT_ID),
        (_CENTER_LEFT_ID, _UPPER_LEFT_ID), (_UPPER_CENTER_ID, _UPPER_RIGHT_ID)
    ])

    return graph


def p4(graph, mapping):
    """ P4 production

    Parameters:
        graph (nx.Graph): graph on which production will be applied.

        mapping (dict):
            keys are ids of template production left side graph (from
            generate_p4_left_side_graph()),
            values are corresponding ids from graph, where we need to apply production

    Returns:
        Nothing. applies production on argument graph in place or raises an error if input not valid.
    """
    if not is_input_valid(graph, mapping):
        raise Exception("Expected right input")

    max_id = graph.graph["max_id"]
    curr_level = graph.nodes[mapping[_CENTER_ID]]['level'] + 1

    graph.graph["max_id"] = max_id + 13
    graph.graph['max_level'] = max(curr_level, graph.graph['max_level'])

    graph.nodes[mapping[_CENTER_ID]]['label'] = 'i'
    graph.nodes[mapping[_CENTER_ID]]['color'] = "brown"

    graph.add_nodes_from([
        (max_id + 1, {"label": "E", "color": "green", "level": curr_level, "pos": graph.nodes[mapping[_UPPER_LEFT_ID]]["pos"]}),
        (max_id + 2, {"label": "E", "color": "green", "level": curr_level, "pos": graph.nodes[mapping[_UPPER_RIGHT_ID]]["pos"]}),
        (max_id + 3, {"label": "E", "color": "green", "level": curr_level, "pos": graph.nodes[mapping[_LOWER_LEFT_ID]]["pos"]}),
        (max_id + 4, {"label": "E", "color": "green", "level": curr_level, "pos": graph.nodes[mapping[_LOWER_RIGHT_ID]]["pos"]}),

        (max_id + 5, {"label": "E", "color": "green", "level": curr_level, "pos": graph.nodes[mapping[_CENTER_LEFT_ID]]["pos"]}),
        (max_id + 6, {"label": "E", "color": "green", "level": curr_level, "pos": calculate_avg(graph.nodes[mapping[_UPPER_LEFT_ID]]["pos"], graph.nodes[mapping[_UPPER_RIGHT_ID]]["pos"])}),
        (max_id + 7, {"label": "E", "color": "green", "level": curr_level, "pos": calculate_avg(graph.nodes[mapping[_UPPER_RIGHT_ID]]["pos"], graph.nodes[mapping[_LOWER_RIGHT_ID]]["pos"])}),
        (max_id + 8, {"label": "E", "color": "green", "level": curr_level, "pos": calculate_avg(graph.nodes[mapping[_LOWER_LEFT_ID]]["pos"], graph.nodes[mapping[_LOWER_RIGHT_ID]]["pos"])}),
    ])

    graph.add_nodes_from([
        (max_id + 9, {"label": "E", "color": "green", "level": curr_level, "pos": calculate_avg(graph.nodes[max_id + 6]["pos"], graph.nodes[max_id + 8]["pos"])}),
        ])

    graph.add_nodes_from([
        (max_id + 10, {"label": "I", "color": "orange", "level": curr_level, "pos": calculate_I_pos(graph.nodes[max_id + 1]["pos"], graph.nodes[max_id + 6]["pos"], graph.nodes[max_id + 9]["pos"], graph.nodes[max_id + 5]["pos"])}),
        (max_id + 11, {"label": "I", "color": "orange", "level": curr_level, "pos": calculate_I_pos(graph.nodes[max_id + 6]["pos"], graph.nodes[max_id + 2]["pos"], graph.nodes[max_id + 7]["pos"], graph.nodes[max_id + 9]["pos"])}),
        (max_id + 12, {"label": "I", "color": "orange", "level": curr_level, "pos": calculate_I_pos(graph.nodes[max_id + 9]["pos"], graph.nodes[max_id + 7]["pos"], graph.nodes[max_id + 4]["pos"], graph.nodes[max_id + 8]["pos"])}),
        (max_id + 13, {"label": "I", "color": "orange", "level": curr_level, "pos": calculate_I_pos(graph.nodes[max_id + 5]["pos"], graph.nodes[max_id + 9]["pos"], graph.nodes[max_id + 8]["pos"], graph.nodes[max_id + 3]["pos"])}),
    ])

    graph.add_edges_from([
        (mapping[_CENTER_ID], max_id + 10), (mapping[_CENTER_ID], max_id + 11), (mapping[_CENTER_ID], max_id + 12), (mapping[_CENTER_ID], max_id + 13),
        (max_id + 1, max_id + 5), (max_id + 1, max_id + 6),
        (max_id + 6, max_id + 9), (max_id + 6, max_id + 2),
        (max_id + 2, max_id + 7),
        (max_id + 7, max_id + 9), (max_id + 7, max_id + 4),
        (max_id + 4, max_id + 8),
        (max_id + 8, max_id + 9), (max_id + 8, max_id + 3),
        (max_id + 3, max_id + 5),
        (max_id + 5, max_id + 9),

        (max_id + 10, max_id + 1), (max_id + 10, max_id + 6), (max_id + 10, max_id + 9), (max_id + 10, max_id + 5),
        (max_id + 11, max_id + 6), (max_id + 11, max_id + 2), (max_id + 11, max_id + 7), (max_id + 11, max_id + 9),
        (max_id + 12, max_id + 9), (max_id + 12, max_id + 7), (max_id + 12, max_id + 4), (max_id + 12, max_id + 8),
        (max_id + 13, max_id + 5), (max_id + 13, max_id + 9), (max_id + 13, max_id + 8), (max_id + 13, max_id + 3)
    ])


def is_input_valid(graph, mapping):
    return True     # TODO: add validation

import networkx as nx

from utils.calculate_position import calculate_I_pos, calculate_avg

_UPPER_LEFT_ID = 8
_UPPER_RIGHT_ID = 9
_LOWER_RIGHT_ID = 15
_LOWER_LEFT_ID = 10
_CENTER_ID = 26


def generate_c_left_side_graph():
    """ Generates template p2 production left side graph

        Returns:
            nx.Graph which should be used in finding subgraph strategy.
        """
    graph = nx.Graph(id="left_c")

    graph.add_nodes_from([
        (_UPPER_LEFT_ID, {"label": "E"}),
        (_UPPER_RIGHT_ID, {"label": "E"}),
        (_LOWER_LEFT_ID, {"label": "E"}),
        (_LOWER_RIGHT_ID, {"label": "E"}),
        (_CENTER_ID, {"label": "I"})
    ])

    graph.add_edges_from([
        (_CENTER_ID, _UPPER_LEFT_ID), (_CENTER_ID, _UPPER_RIGHT_ID), (_CENTER_ID, _LOWER_LEFT_ID), (_CENTER_ID, _LOWER_RIGHT_ID),
        (_UPPER_LEFT_ID, _UPPER_RIGHT_ID), (_UPPER_RIGHT_ID, _LOWER_RIGHT_ID), (_LOWER_RIGHT_ID, _LOWER_LEFT_ID), (_LOWER_LEFT_ID, _UPPER_LEFT_ID),
    ])

    return graph


def c(graph, mapping):
    """ C production

    Parameters:
        graph (nx.Graph): graph on which production will be applied.

        mapping (dict):
            keys are ids of template production left side graph (from generate_p2_left_side_graph()),
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

        (max_id + 5, {"label": "E", "color": "green", "level": curr_level, "pos": calculate_avg(graph.nodes[mapping[_UPPER_LEFT_ID]]["pos"], graph.nodes[mapping[_UPPER_RIGHT_ID]]["pos"])}),
        (max_id + 6, {"label": "E", "color": "green", "level": curr_level, "pos": calculate_avg(graph.nodes[mapping[_UPPER_RIGHT_ID]]["pos"], graph.nodes[mapping[_LOWER_RIGHT_ID]]["pos"])}),
        (max_id + 7, {"label": "E", "color": "green", "level": curr_level, "pos": calculate_avg(graph.nodes[mapping[_LOWER_LEFT_ID]]["pos"], graph.nodes[mapping[_LOWER_RIGHT_ID]]["pos"])}),
        (max_id + 8, {"label": "E", "color": "green", "level": curr_level, "pos": calculate_avg(graph.nodes[mapping[_UPPER_LEFT_ID]]["pos"], graph.nodes[mapping[_LOWER_LEFT_ID]]["pos"])}),
        (max_id + 9, {"label": "E", "color": "green", "level": curr_level, "pos": calculate_avg(graph.nodes[mapping[_UPPER_LEFT_ID]]["pos"], graph.nodes[mapping[_LOWER_RIGHT_ID]]["pos"])}),
    ])

    pos = [
        (calculate_I_pos(graph.nodes[max_id + 1]["pos"], graph.nodes[max_id + 5]["pos"], graph.nodes[max_id + 8]["pos"],
                         graph.nodes[max_id + 9]["pos"]), 0),
        (calculate_I_pos(graph.nodes[max_id + 5]["pos"], graph.nodes[max_id + 2]["pos"], graph.nodes[max_id + 9]["pos"],
                         graph.nodes[max_id + 6]["pos"]), 1),
        (calculate_I_pos(graph.nodes[max_id + 8]["pos"], graph.nodes[max_id + 9]["pos"], graph.nodes[max_id + 3]["pos"],
                         graph.nodes[max_id + 7]["pos"]), 2),
        (calculate_I_pos(graph.nodes[max_id + 9]["pos"], graph.nodes[max_id + 6]["pos"], graph.nodes[max_id + 7]["pos"],
                         graph.nodes[max_id + 4]["pos"]), 3),
    ]
    sorted_pos = sorted(pos, key=lambda x: x[0][0])

    graph.add_nodes_from([
        (max_id + 10, {"label": "i" if sorted_pos[0][1] == 0 or sorted_pos[1][1] == 0 else "I", "color": "aqua" if sorted_pos[0][1] == 0 or sorted_pos[1][1] == 0 else "orange", "level": curr_level, "pos": pos[0][0]}),
        (max_id + 11, {"label": "i" if sorted_pos[0][1] == 1 or sorted_pos[1][1] == 1 else "I", "color": "aqua" if sorted_pos[0][1] == 1 or sorted_pos[1][1] == 1 else "orange", "level": curr_level, "pos": pos[1][0]}),
        (max_id + 12, {"label": "i" if sorted_pos[0][1] == 2 or sorted_pos[1][1] == 2 else "I", "color": "aqua" if sorted_pos[0][1] == 2 or sorted_pos[1][1] == 2 else "orange", "level": curr_level, "pos": pos[2][0]}),
        (max_id + 13, {"label": "i" if sorted_pos[0][1] == 3 or sorted_pos[1][1] == 3 else "I", "color": "aqua" if sorted_pos[0][1] == 3 or sorted_pos[1][1] == 3 else "orange", "level": curr_level, "pos": pos[3][0]}),
    ])

    graph.add_edges_from([
        (mapping[_CENTER_ID], max_id + 10), (mapping[_CENTER_ID], max_id + 11), (mapping[_CENTER_ID], max_id + 12), (mapping[_CENTER_ID], max_id + 13),
        (max_id + 1, max_id + 5), (max_id + 1, max_id + 8), (max_id + 9, max_id + 5), (max_id + 9, max_id + 8),
        (max_id + 5, max_id + 2), (max_id + 2, max_id + 6), (max_id + 6, max_id + 9),
        (max_id + 8, max_id + 3), (max_id + 3, max_id + 7), (max_id + 7, max_id + 9),
        (max_id + 7, max_id + 4), (max_id + 4, max_id + 6),

        (max_id + 10, max_id + 1), (max_id + 10, max_id + 5), (max_id + 10, max_id + 8), (max_id + 10, max_id + 9),
        (max_id + 11, max_id + 5), (max_id + 11, max_id + 2), (max_id + 11, max_id + 9), (max_id + 11, max_id + 6),
        (max_id + 12, max_id + 8), (max_id + 12, max_id + 9), (max_id + 12, max_id + 3), (max_id + 12, max_id + 7),
        (max_id + 13, max_id + 9), (max_id + 13, max_id + 6), (max_id + 13, max_id + 7), (max_id + 13, max_id + 4)
    ])


def is_input_valid(graph, mapping):
    return True     # TODO: add validation

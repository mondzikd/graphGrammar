import networkx as nx

_E_GREEN_ID = 0
_I_ORANGE_LEFT_ID = 1
_I_ORANGE_RIGHT_ID = 2
_E_YELLOW_UP_ID = 3
_E_YELLOW_DOWN_ID = 4
_E_YELLOW_LEFT_ID = 5
_E_YELLOW_RIGHT_ID = 6
_I_GREY_UP_LEFT_ID = 7
_I_GREY_UP_RIGHT_ID = 8
_I_GREY_DOWN_LEFT_ID = 9
_I_GREY_DOWN_RIGHT_ID = 10


def swap_dictionary(dictionary):
    return {value: key for key, value in dictionary.items()}


def generate_p9_left_side_graph():
    graph = nx.Graph(id="left_p9")

    graph.add_nodes_from(
        [
            (_E_GREEN_ID, {"label": "E"}),
            (_I_ORANGE_LEFT_ID, {"label": "i"}),
            (_I_ORANGE_RIGHT_ID, {"label": "i"}),
            (_E_YELLOW_UP_ID, {"label": "E"}),
            (_E_YELLOW_DOWN_ID, {"label": "E"}),
            (_E_YELLOW_LEFT_ID, {"label": "E"}),
            (_E_YELLOW_RIGHT_ID, {"label": "E"}),
            (_I_GREY_UP_LEFT_ID, {"label": "I"}),
            (_I_GREY_UP_RIGHT_ID, {"label": "I"}),
            (_I_GREY_DOWN_LEFT_ID, {"label": "I"}),
            (_I_GREY_DOWN_RIGHT_ID, {"label": "I"}),
        ]
    )

    graph.add_edges_from(
        [
            (_E_GREEN_ID, _I_ORANGE_LEFT_ID),
            (_E_GREEN_ID, _I_ORANGE_RIGHT_ID),
            (_I_ORANGE_LEFT_ID, _I_GREY_UP_LEFT_ID),
            (_I_ORANGE_LEFT_ID, _I_GREY_DOWN_LEFT_ID),
            (_I_ORANGE_RIGHT_ID, _I_GREY_UP_RIGHT_ID),
            (_I_ORANGE_RIGHT_ID, _I_GREY_DOWN_RIGHT_ID),
            (_I_GREY_UP_LEFT_ID, _E_YELLOW_UP_ID),
            (_I_GREY_UP_LEFT_ID, _E_YELLOW_LEFT_ID),
            (_I_GREY_DOWN_LEFT_ID, _E_YELLOW_LEFT_ID),
            (_I_GREY_DOWN_LEFT_ID, _E_YELLOW_DOWN_ID),
            (_I_GREY_UP_RIGHT_ID, _E_YELLOW_UP_ID),
            (_I_GREY_UP_RIGHT_ID, _E_YELLOW_RIGHT_ID),
            (_I_GREY_DOWN_RIGHT_ID, _E_YELLOW_RIGHT_ID),
            (_I_GREY_DOWN_RIGHT_ID, _E_YELLOW_DOWN_ID),
            (_E_YELLOW_LEFT_ID, _E_YELLOW_UP_ID),
            (_E_YELLOW_LEFT_ID, _E_YELLOW_DOWN_ID),
            (_E_YELLOW_RIGHT_ID, _E_YELLOW_UP_ID),
            (_E_YELLOW_RIGHT_ID, _E_YELLOW_DOWN_ID),
        ]
    )

    return graph


def find_all_p9_mappings(graph):
    template_subgraph = generate_p9_left_side_graph()
    graph_matcher = nx.algorithms.isomorphism.GraphMatcher(
        graph, template_subgraph, node_match=lambda n1, n2: n1["label"] == n2["label"]
    )

    return list(graph_matcher.subgraph_isomorphisms_iter())


def validate_p9_mapping(graph, mapping):
    """Checks if coordinates of nodes included in the mapping match constraints"""
    # mapping: graph node -> template subgraph node
    # swap_mapping: template subgraph node -> graph node
    swap_mapping = swap_dictionary(mapping)

    # Get IDs and nodes from the original graph
    e_yellow_up_id = swap_mapping[_E_YELLOW_UP_ID]
    e_yellow_left_id = swap_mapping[_E_YELLOW_LEFT_ID]
    e_yellow_right_id = swap_mapping[_E_YELLOW_RIGHT_ID]
    e_yellow_down_id = swap_mapping[_E_YELLOW_DOWN_ID]

    e_yellow_up = graph.nodes[e_yellow_up_id]
    e_yellow_left = graph.nodes[e_yellow_left_id]
    e_yellow_right = graph.nodes[e_yellow_right_id]
    e_yellow_down = graph.nodes[e_yellow_down_id]

    if e_yellow_left["pos"] != e_yellow_right["pos"]:
        return False

    (x1, y1) = e_yellow_up["pos"]
    (x2, y2) = e_yellow_down["pos"]

    x3 = (x1 + x2) / 2.0
    y3 = (y1 + y2) / 2.0

    return e_yellow_left["pos"] == (x3, y3)


def take_first(mappings):
    if len(mappings) == 0:
        raise Exception("P9 cannot be applied!")

    return mappings[0]


def p9(graph, strategy=take_first):
    mappings = find_all_p9_mappings(graph)
    mappings = list(filter(lambda m: validate_p9_mapping(graph, m), mappings))

    mapping = strategy(mappings)
    swap_mapping = swap_dictionary(mapping)

    # Get IDs and nodes from the original graph
    e_yellow_left_id = swap_mapping[_E_YELLOW_LEFT_ID]
    e_yellow_right_id = swap_mapping[_E_YELLOW_RIGHT_ID]
    i_grey_up_right_id = swap_mapping[_I_GREY_UP_RIGHT_ID]
    i_grey_down_right_id = swap_mapping[_I_GREY_DOWN_RIGHT_ID]

    graph.remove_node(e_yellow_right_id)
    graph.add_edges_from(
        [
            (e_yellow_left_id, i_grey_up_right_id),
            (e_yellow_left_id, i_grey_down_right_id),
        ]
    )

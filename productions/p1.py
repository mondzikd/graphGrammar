from utils.calculate_position import calculate_I_pos


def p1(graph, pos=None):
    """ P1 production

        Parameters:
            graph (nx.Graph): graph on which production will be applied.

            pos (dict): nodes positions
                keys - 1 for upper left node, 2 for upper right node, 3 for lower left node, 4 for lower right node,
                values - corresponding initial coordinates (x, y)

        Returns:
            Nothing. applies production on argument graph in place or raises an error if input not valid.
    """
    if not is_graph_valid(graph):
        raise Exception("Expected starting graph: [0 {'label': 'e', 'color': 'red'}]")
    if not is_pos_valid(pos):
        raise Exception("Expected 'pos' argument: {1: (x1, y1), 2: (x2, y2), 3: (x3, y3), 4: (x4, y4)}")

    if pos is None:
        pos = {1: (0, 1), 2: (1, 1), 3: (0, 0), 4: (1, 0)}

    graph.add_nodes_from([
        (1, {"label": 'E', "color": "blue", "level": 1, "pos": pos[1]}),
        (2, {"label": "E", "color": "blue", "level": 1, "pos": pos[2]}),
        (3, {"label": "E", "color": "blue", "level": 1, "pos": pos[3]}),
        (4, {"label": "E", "color": "blue", "level": 1, "pos": pos[4]}),
        (5, {"label": "I", "color": "brown", "level": 1, "pos": calculate_I_pos(pos[1], pos[2], pos[3], pos[4])})
    ])

    graph.nodes[0]["label"] = "e"

    graph.add_edges_from([
        (0, 5),
        (5, 1), (5, 2), (5, 3), (5, 4),
        (1, 2), (2, 4), (4, 3), (3, 1),
    ])

    graph.graph['max_id'] = 5
    graph.graph['max_level'] = 1


def is_graph_valid(graph):
    return len(graph.nodes) == 1 and \
           list(graph.nodes)[0] == 0 and \
           'label' in graph.nodes[0].keys() and \
           graph.nodes[0]['label'] == 'S'


def is_pos_valid(pos):
    return True     # TODO: add validation

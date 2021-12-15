from utils.calculate_position import calculate_I_pos, calculate_e_pos


def p1(graph, pos=None):
    if is_p1_input_valid(graph):
        if pos is None:     # TODO: add pos validation
            pos = {1: (0, 1), 2: (1, 1), 3: (0, 0), 4: (1, 0)}

        graph.add_nodes_from([
            (1, {"label": 'E', "color": "blue", "pos": pos[1]}),
            (2, {"label": "E", "color": "blue", "pos": pos[2]}),
            (3, {"label": "E", "color": "blue", "pos": pos[3]}),
            (4, {"label": "E", "color": "blue", "pos": pos[4]}),
            (5, {"label": "I", "color": "brown", "pos": calculate_I_pos(pos)})
        ])

        graph.nodes[0]["pos"] = calculate_e_pos(pos)

        graph.add_edges_from([
            (0, 5),
            (5, 1), (5, 2), (5, 3), (5, 4),
            (1, 2), (2, 4), (4, 3), (3, 1),
        ])
    else:
        raise Exception("Expected starting graph: [0 {'label': 'e', 'color': 'red'}]")


def is_p1_input_valid(graph):
    return len(graph.nodes) == 1 and \
           list(graph.nodes)[0] == 0 and \
           set(graph.nodes[0].keys()) == {'label', 'color'} and \
           graph.nodes[0]['label'] == 'e' and \
           graph.nodes[0]['color'] == 'red'

from enum import Enum


class Strategy(Enum):
    ID = 1
    VERTICAL = 2
    HORIZONTAL = 3


def p8(graph, n=None, strategy=Strategy.ID):
    nodes_with_data = graph.nodes(data=True)
    max_level = max(map(lambda x: x[1]['level'], nodes_with_data))
    deepest_nodes = filter(lambda x: x[1]['level'] == max_level, nodes_with_data)

    nodes = dict(deepest_nodes)
    nodes_to_merge = []

    for node_id, data in nodes.items():
        node_pos = nodes[node_id]['pos']
        node_neighbors = get_neighbors_by_pos(graph, nodes, node_id, strategy)

        for neighbor_pos, neighbor_ids in node_neighbors.items():
            if len(neighbor_ids) == 2:
                expected_nodes_to_merge_pos = tuple(map(lambda i, j: j + (i - j) * 2, neighbor_pos, node_pos))
                nodes_to_merge.append(get_nodes_to_merge(graph, nodes, neighbor_ids, expected_nodes_to_merge_pos))

    if n is not None and n > 0:
        nodes_to_merge = nodes_to_merge[:n]
    # nodes_to_merge is a list of lists
    for ntm in nodes_to_merge:
        for node_1, node_2 in ntm:
            _merge_nodes(graph, node_1, node_2)


def follows_strategy(strategy, node_pos, neighbor_pos):
    x1, y1 = node_pos
    x2, y2 = neighbor_pos
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)

    if strategy == Strategy.VERTICAL:
        return delta_y > delta_x
    elif strategy == Strategy.HORIZONTAL:
        return delta_x > delta_y
    else:
        return True


def get_neighbors_by_pos(graph, nodes, node_id, strategy):
    node_neighbors = {}
    for neighbor_id in list(graph.neighbors(node_id)):
        if is_E_node(nodes, neighbor_id):
            neighbor_pos = nodes[neighbor_id]["pos"]
            node_pos = nodes[node_id]["pos"]
            if follows_strategy(strategy, node_pos, neighbor_pos):
                node_neighbors.setdefault(neighbor_pos, []).append(neighbor_id)
    return node_neighbors


def get_nodes_to_merge(graph, nodes, neighbor_ids, expected_nodes_to_merge_pos):
    nodes_to_merge = []
    neighbors_to_merge = []  # koncowe wezly E
    for neighbor_id in neighbor_ids:
        for neighbor_2_id in list(graph.neighbors(neighbor_id)):
            if is_E_node(nodes, neighbor_2_id) and has_position(nodes, neighbor_2_id, expected_nodes_to_merge_pos):
                neighbors_to_merge.append(neighbor_2_id)
    if len(neighbors_to_merge) == 2:
        nodes_to_merge.append((neighbor_ids[0], neighbor_ids[1]))  # srodkowe wezly "E"
        nodes_to_merge.append((neighbors_to_merge[0], neighbors_to_merge[1]))  # koncowe wezly "E"
    return nodes_to_merge


def is_E_node(nodes, node_id):
    try:
        return nodes[node_id]['label'] == 'E'
    except KeyError:
        return False


def has_position(nodes, node_id, position):
    try:
        return nodes[node_id]["pos"] == position
    except KeyError:
        return False


def _merge_nodes(graph, node_1, node_2):
    n1 = min(node_1, node_2)
    n2 = max(node_1, node_2)
    edges_to_remove = list(graph.edges(n2))
    edges_to_add = [tuple([node_id if node_id != n2 else n1 for node_id in node_ids]) for node_ids in edges_to_remove]

    graph.remove_edges_from(edges_to_remove)
    graph.remove_node(n2)
    graph.add_edges_from(edges_to_add)

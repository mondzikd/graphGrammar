import networkx as nx
import matplotlib.pyplot as plt


def move_up(pos, distance):
    x, y = pos
    return x, y + distance


def visualize(graph, level=None):   # TODO: Refactor
    if level is not None and level <= graph.graph["max_level"]:
        subgraph_nodes = [node_id for node_id in graph.nodes if graph.nodes[node_id].get("level", 1) == level]
        graph = nx.subgraph(graph, subgraph_nodes)
        color_map = list(map(lambda node_id: graph.nodes[node_id].get('color', 'red'), graph.nodes))
        label_dict = dict(map(lambda node_id: (node_id, graph.nodes[node_id]['label']), graph.nodes))
        pos = nx.get_node_attributes(graph, 'pos')
    else:
        graph_height = max(graph.nodes[0]["pos"][1], graph.nodes[1]["pos"][1], graph.nodes[2]["pos"][1], graph.nodes[3]["pos"][1]) - min(graph.nodes[0]["pos"][1], graph.nodes[1]["pos"][1], graph.nodes[2]["pos"][1], graph.nodes[3]["pos"][1])
        color_map = list(map(lambda node_id: graph.nodes[node_id].get('color', 'red'), graph.nodes))
        label_dict = dict(map(lambda node_id: (node_id, graph.nodes[node_id]['label']), graph.nodes))
        pos = {node_id: move_up(graph.nodes[node_id]["pos"], graph.nodes[node_id].get("level", 1) * graph_height * 2) for node_id in graph.nodes}

    nx.draw(graph, pos=pos, node_color=color_map, labels=label_dict, with_labels=True)
    plt.show()  # TODO: while visualizing all levels in one picture, change dimensions of that picture to be more rectangular (and readable)

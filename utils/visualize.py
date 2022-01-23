import networkx as nx
import matplotlib.pyplot as plt


def move_up(pos, distance):
    x, y = pos
    return x, y + distance


def visualize(graph, level=None):   # TODO: Refactor
    if level is not None and level <= graph.graph["max_level"]:
        subgraph_nodes = [node_id for node_id in graph.nodes if graph.nodes[node_id]["level"] == level]
        graph = nx.subgraph(graph, subgraph_nodes)
        color_map = list(map(lambda node_id: graph.nodes[node_id]['color'], graph.nodes))
        label_dict = dict(map(lambda node_id: (node_id, graph.nodes[node_id]['label']), graph.nodes))
        pos = nx.get_node_attributes(graph, 'pos')
    else:
        color_map = list(map(lambda node_id: graph.nodes[node_id]['color'], graph.nodes))
        label_dict = dict(map(lambda node_id: (node_id, graph.nodes[node_id]['label']), graph.nodes))
        pos = nx.get_node_attributes(graph, 'pos')

    nx.draw(graph, pos=pos, node_color=color_map, labels=label_dict, with_labels=True)
    plt.show()  # TODO: while visualizing all levels in one picture, change dimensions of that picture to be more rectangular (and readable)

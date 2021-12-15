import networkx as nx
import matplotlib.pyplot as plt


def visualize(graph, level=None):   # TODO: add visualizing level handling
    color_map = list(map(lambda node: graph.nodes[node]['color'], graph.nodes))
    label_dict = dict(map(lambda node: (node, graph.nodes[node]['label']), graph))
    pos = nx.get_node_attributes(graph, 'pos')

    nx.draw(graph, pos=pos, node_color=color_map, labels=label_dict, with_labels=True)
    plt.show()

import networkx as nx


def initialize():
    graph = nx.Graph()
    graph.add_node(0, label='e', color="red")
    return graph

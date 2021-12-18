import networkx as nx


def initialize(pos=(0.5, 1.5)):
    graph = nx.Graph(max_id=0, max_level=0)  # TODO: add max_id, max_level
    graph.add_node(0, label='S', color="red", level=0, pos=pos)
    return graph

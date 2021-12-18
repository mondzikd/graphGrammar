from random import randint
import networkx as nx


def swap_keys_and_values(dictionary):
    return {value: key for key, value in dictionary.items()}


def super_simple_strategy(graph, template_subgraph):
    """ Example strategy for proper subgraph finding

        Parameters:
            graph (nx.Graph): Graph where subgraph nodes ids are requested.

            template_subgraph (nx.Graph): Template for requested subgraph.
                                          In out case this should be left side of production.

        Returns:
            Dictionary, which maps template_subgraph nodes ids to found subgraph nodes ids from graph.
        """
    graph_matcher = nx.algorithms.isomorphism.GraphMatcher(graph, template_subgraph, node_match=lambda n1, n2: n1["label"] == n2["label"])
    subgraph_list = list(graph_matcher.subgraph_isomorphisms_iter())

    # dictionary = subgraph_list[randint(0, len(subgraph_list)-1)]
    dictionary = subgraph_list[0]
    return swap_keys_and_values(dictionary)

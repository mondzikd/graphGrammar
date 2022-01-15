import networkx as nx


def swap_keys_and_values(dictionary):
    return {value: key for key, value in dictionary.items()}


def p3_p4_strategy(graph, template_subgraph):
    """ Example strategy for proper subgraph finding

        Parameters:
            graph (nx.Graph): Graph where subgraph nodes ids are requested.

            template_subgraph (nx.Graph): Template for requested subgraph.
                                          In out case this should be left side of production.

        Returns:
            Dictionary, which maps template_subgraph nodes ids to found subgraph nodes ids from graph.
        """

    for node_id in graph.nodes:
        neighbors = [n for n in graph.neighbors(node_id)]
        if len(neighbors) != 2:
            continue
        first_pos = graph.nodes[neighbors[0]]["pos"]
        second_pos = graph.nodes[neighbors[1]]["pos"]
        graph.nodes[node_id]["is_equidistant"] = first_pos[0] + second_pos[
            0] == 2 * graph.nodes[node_id]["pos"][0] and first_pos[1] + \
                                                 second_pos[1] == 2 * \
                                                 graph.nodes[node_id]["pos"][1]

    def match(n1, n2):
        if n1["label"] != n2["label"]:
            return False
        if not n2["should_equidistant"]:
            return True
        return "is_equidistant" not in n1 or n1["is_equidistant"]
    graph_matcher = nx.algorithms.isomorphism.GraphMatcher(graph, template_subgraph,
                                                           node_match=match)
    subgraph_list = list(graph_matcher.subgraph_isomorphisms_iter())
    print(subgraph_list)

    dictionary = subgraph_list[0]
    return swap_keys_and_values(dictionary)

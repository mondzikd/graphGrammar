import networkx as nx

from productions.p1 import p1
from productions.p2 import generate_p2_left_side_graph, p2
from utils.initialize import initialize
from utils.visualize import visualize


def swap_keys_and_values(dictionary):
    return {value: key for key, value in dictionary.items()}


def find_all_mappings(graph, template_subgraph):
    graph_matcher = nx.algorithms.isomorphism.GraphMatcher(graph, template_subgraph,
                                                           node_match=lambda n1, n2: n1["label"] == n2["label"])
    return [swap_keys_and_values(d) for d in list(graph_matcher.subgraph_isomorphisms_iter())]


def main():
    graph = initialize((0., 0.))
    spread = 100
    p1(graph, {1: (0, spread), 2: (spread, spread), 3: (0, 0), 4: (spread, 0)})

    left_side = generate_p2_left_side_graph()

    I_id = 26

    def is_max_lvl_mapping(mapping):
        I_graph_id = mapping[I_id]
        I_graph = dict(list(graph.nodes(data=True))).get(I_graph_id)
        I_lvl = I_graph['level']
        return I_lvl == graph.graph['max_level']

    def get_I_x_coord(mapping):
        I_graph_id = mapping[I_id]
        I_graph = dict(list(graph.nodes(data=True))).get(I_graph_id)
        return I_graph['pos'][0]

    def get_unique_mappings(mappings):
        unique_mappings = []
        unique_mappings_indices = set()
        for m in mappings:
            s_indices = frozenset(m.values())
            if s_indices not in unique_mappings_indices:
                unique_mappings.append(m)
                unique_mappings_indices.add(s_indices)
        return unique_mappings

    # keys are template graph IDs, values are 'graph' IDs
    for level in range(5):
        visualize(graph)
        print(graph.graph['max_level'])
        repeats = 2 ** level

        p2_mappings = find_all_mappings(graph, left_side)

        # find mappings having I with max level attribute
        p2_mappings = list(filter(is_max_lvl_mapping, p2_mappings))
        p2_mappings = get_unique_mappings(p2_mappings)

        # select 2 mapping with the biggest sum of X coordinate
        p2_mappings = [(get_I_x_coord(m), m) for m in p2_mappings]
        p2_mappings.sort(key=lambda t: t[0], reverse=True)
        p2_mappings = p2_mappings[:repeats]
        print(f'Len: {len(p2_mappings)}')

        for (x, mapping) in p2_mappings:
            print(f'applying to I at {x} {mapping}')
            p2(graph, mapping)

    visualize(graph)


if __name__ == '__main__':
    main()

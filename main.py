from products.p1 import p1
from products.p2 import generate_p2_left_side_graph, p2
from strategies.super_simple_strategy import super_simple_strategy
from utils.initialize import initialize
from utils.visualize import visualize


def main():
    graph = initialize()
    p1(graph)
    # p1(graph, pos={1: (-2, 3), 2: (3, 2), 3: (-1, -2), 4: (2, -2)})

    left_side = generate_p2_left_side_graph()
    p2(graph, super_simple_strategy(graph, left_side))

    left_side = generate_p2_left_side_graph()
    p2(graph, super_simple_strategy(graph, left_side))

    left_side = generate_p2_left_side_graph()
    p2(graph, super_simple_strategy(graph, left_side))

    # visualize(graph)
    visualize(graph, level=3)


if __name__ == '__main__':
    main()

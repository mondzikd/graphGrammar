from productions.p1 import p1
from productions.p2 import generate_p2_left_side_graph, p2
from productions.p3 import generate_p3_left_side_graph, p3, generate_p3_left_side_graph_test
from strategies.super_simple_strategy import super_simple_strategy
from utils.initialize import initialize
from utils.visualize import visualize


def main():
    graph = initialize()
    p1(graph)
    # p1(graph, pos={1: (-2, 3), 2: (3, 2), 3: (-1, -2), 4: (2, -2)})

    # left_side = generate_p2_left_side_graph()
    # p2(graph, super_simple_strategy(graph, left_side))
    #
    # left_side = generate_p2_left_side_graph()
    # p2(graph, super_simple_strategy(graph, left_side))
    #
    # left_side = generate_p2_left_side_graph()
    # p2(graph, super_simple_strategy(graph, left_side))
    #

    test_p3 = generate_p3_left_side_graph_test()
    visualize(test_p3, level=2)

    left_side_p3 = generate_p3_left_side_graph()
    p3(test_p3, super_simple_strategy(test_p3, left_side_p3))
    visualize(test_p3, level=3)



    # visualize(graph)
    # visualize(graph, level=3)


if __name__ == '__main__':
    main()

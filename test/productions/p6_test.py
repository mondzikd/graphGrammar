from productions.p6 import p6, generate_p6_left_side_graph, generate_p6_test_correct, \
    generate_p6_test_incorrect_position, generate_p6_test_incorrect_labels, \
    generate_p6_test_missing_vertex, generate_p6_test_missing_edge, generate_bigger_p6_1_test, generate_bigger_p6_2_test
from strategies.super_simple_strategy import super_simple_strategy
from utils.visualize import visualize


def valid_graph_test():
    left_side_p6 = generate_p6_left_side_graph()
    p6_correct = generate_p6_test_correct()
    visualize(p6_correct, level=2)
    p6(p6_correct, super_simple_strategy(p6_correct, left_side_p6))
    visualize(p6_correct, level=3)


def invalid_position_test():
    left_side_p6 = generate_p6_left_side_graph()
    p6_incorrect_pos = generate_p6_test_incorrect_position()
    visualize(p6_incorrect_pos, level=2)
    p6(p6_incorrect_pos, super_simple_strategy(p6_incorrect_pos, left_side_p6))
    visualize(p6_incorrect_pos, level=3)


def invalid_labels_test():
    left_side_p6 = generate_p6_left_side_graph()
    p6_incorrect_label = generate_p6_test_incorrect_labels()
    visualize(p6_incorrect_label, level=2)
    p6(p6_incorrect_label, super_simple_strategy(p6_incorrect_label, left_side_p6))
    visualize(p6_incorrect_label, level=3)


def missing_vertex_test():
    left_side_p6 = generate_p6_left_side_graph()
    p6_missing_vertex = generate_p6_test_missing_vertex()
    visualize(p6_missing_vertex, level=2)
    p6(p6_missing_vertex, super_simple_strategy(p6_missing_vertex, left_side_p6))
    visualize(p6_missing_vertex, level=3)


def missing_edge_test():
    left_side_p6 = generate_p6_left_side_graph()
    p6_missing_edge = generate_p6_test_missing_edge()
    visualize(p6_missing_edge, level=2)
    p6(p6_missing_edge, super_simple_strategy(p6_missing_edge, left_side_p6))
    visualize(p6_missing_edge, level=3)


def bigger_graph_1_test():
    left_side_p6 = generate_p6_left_side_graph()
    p6_bigger_graph = generate_bigger_p6_1_test()
    visualize(p6_bigger_graph, level=2)
    p6(p6_bigger_graph, super_simple_strategy(p6_bigger_graph, left_side_p6))
    visualize(p6_bigger_graph, level=3)


def bigger_graph_2_test():
    left_side_p6 = generate_p6_left_side_graph()
    p6_bigger_graph = generate_bigger_p6_2_test()
    visualize(p6_bigger_graph, level=2)
    p6(p6_bigger_graph, super_simple_strategy(p6_bigger_graph, left_side_p6))
    visualize(p6_bigger_graph, level=3)


if __name__ == '__main__':
    # valid_graph_test()
    # invalid_position_test()
    # invalid_labels_test()
    # missing_vertex_test()
    # missing_edge_test()
    # bigger_graph_1_test()
    bigger_graph_2_test()




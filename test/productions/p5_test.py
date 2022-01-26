from productions.p5 import p5, generate_p5_test_correct, generate_p5_test_incorrect_labels, \
    generate_p5_test_incorrect_position, generate_p5_left_side_graph, generate_p5_test_missing_vertex, \
    generate_p5_test_missing_edge, generate_bigger_p5_1_test, generate_bigger_p5_2_test
from strategies.super_simple_strategy import super_simple_strategy
from utils.visualize import visualize


def valid_graph_test():
    left_side_p5 = generate_p5_left_side_graph()
    p5_correct = generate_p5_test_correct()
    visualize(p5_correct, level=2)
    p5(p5_correct, super_simple_strategy(p5_correct, left_side_p5))
    visualize(p5_correct, level=3)


def invalid_position_test():
    left_side_p5 = generate_p5_left_side_graph()
    p5_incorrect_pos = generate_p5_test_incorrect_position()
    visualize(p5_incorrect_pos, level=2)
    p5(p5_incorrect_pos, super_simple_strategy(p5_incorrect_pos, left_side_p5))
    visualize(p5_incorrect_pos, level=3)


def invalid_labels_test():
    left_side_p5 = generate_p5_left_side_graph()
    p5_incorrect_label = generate_p5_test_incorrect_labels()
    visualize(p5_incorrect_label, level=2)
    p5(p5_incorrect_label, super_simple_strategy(p5_incorrect_label, left_side_p5))
    visualize(p5_incorrect_label, level=3)


def missing_vertex_test():
    left_side_p5 = generate_p5_left_side_graph()
    p5_missing_vertex = generate_p5_test_missing_vertex()
    visualize(p5_missing_vertex, level=2)
    p5(p5_missing_vertex, super_simple_strategy(p5_missing_vertex, left_side_p5))
    visualize(p5_missing_vertex, level=3)


def missing_edge_test():
    left_side_p5 = generate_p5_left_side_graph()
    p5_missing_edge = generate_p5_test_missing_edge()
    visualize(p5_missing_edge, level=2)
    p5(p5_missing_edge, super_simple_strategy(p5_missing_edge, left_side_p5))
    visualize(p5_missing_edge, level=3)


def bigger_graph_1_test():
    left_side_p5 = generate_p5_left_side_graph()
    p5_bigger_graph = generate_bigger_p5_1_test()
    visualize(p5_bigger_graph, level=2)
    p5(p5_bigger_graph, super_simple_strategy(p5_bigger_graph, left_side_p5))
    visualize(p5_bigger_graph, level=3)


def bigger_graph_2_test():
    left_side_p5 = generate_p5_left_side_graph()
    p5_bigger_graph = generate_bigger_p5_2_test()
    visualize(p5_bigger_graph, level=2)
    p5(p5_bigger_graph, super_simple_strategy(p5_bigger_graph, left_side_p5))
    visualize(p5_bigger_graph, level=3)


if __name__ == '__main__':
    # valid_graph_test()
    # invalid_position_test()
    # invalid_labels_test()
    # missing_vertex_test()
    # missing_edge_test()
    bigger_graph_1_test()
    # bigger_graph_2_test()




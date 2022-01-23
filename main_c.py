from productions.p1 import p1
from productions.c import generate_c_left_side_graph, c
from strategies.super_simple_strategy import super_simple_strategy_returning_list
from utils.initialize import initialize
from utils.visualize import visualize


def main():
    graph = initialize()
    p1(graph)

    i = 0
    iterations = 2190
    for _ in range(4):
        left_side = generate_c_left_side_graph()
        for m in super_simple_strategy_returning_list(graph, left_side):
            c(graph, m)
            i += 1
            if i == iterations:
                break
        if i == iterations:
            break
    print(i)

    # visualize(graph)
    visualize(graph, level=7)


if __name__ == '__main__':
    main()

from products.p1 import p1
from utils.initialize import initialize
from utils.visualize import visualize


def main():
    graph = initialize()
    p1(graph, pos={1: (-2, 3), 2: (3, 2), 3: (-1, -2), 4: (2, -2)})

    visualize(graph)


if __name__ == '__main__':
    main()

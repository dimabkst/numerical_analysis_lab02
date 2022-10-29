from typing import Callable, Tuple, List
from math import ceil


def left_rectangle(f: Callable, a: float, b: float, h: float) -> Tuple[float, List[float]]:
    nodes_count = ceil((b - a) / h)
    nodes = [a + h * i for i in range(nodes_count)]
    res = h * sum([f(node) for node in nodes])

    return res, nodes


def trapezoid(f: Callable, a: float, b: float, h: float) -> Tuple[float, List[float]]:
    nodes_count = ceil((b - a) / h) + 1
    nodes = [a + h * i for i in range(nodes_count)]
    res = h * (f(nodes[0]) / 2 + sum([f(node) for node in nodes[1:-1]]) + f(nodes[-1]) / 2)

    return res, nodes


def simpson(f: Callable, a: float, b: float, h: float) -> Tuple[float, List[float]]:
    nodes_count = ceil((b - a) / h) + 1
    nodes = [a + h * i for i in range(nodes_count)]
    res = (h / 6) * (f(nodes[0]) + 4 * sum([f((nodes[i] + nodes[i + 1]) / 2) for i in range(len(nodes) - 1)]) + 2 * sum(
        [f(node) for node in nodes[1:-1]]) + f(nodes[-1]))

    return res, nodes

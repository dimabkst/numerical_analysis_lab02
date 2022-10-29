from typing import Callable, Tuple
import printer


def runge(f: Callable, a: float, b: float, h: float, integral_formula: Callable, p: int) -> Tuple[float, float]:
    I_h, I_half_h = integral_formula(a, b, f, h), integral_formula(a, b, f, h / 2)
    precision = abs(I_half_h - I_h) / (2 ** p - 1)

    return precision, I_half_h


def runge_algorithm(f: Callable, a: float, b: float, h: float, integral_formula: Callable, p: int, epsilon: float):
    N = 0
    h_N = [h]
    I = []
    precisions = [epsilon * 2]  # So while will start
    nodes = []


    printer.task_iter_info(N, h_N[-1], 0, precisions[-1], epsilon, [])
    while precisions[-1] > epsilon:
        if N >= 1:
            h_N.append(h_N[-1] / 2)  # So first step will go without changing h

        I_hN, new_nodes = integral_formula(f, a, b, h_N[-1])
        nodes.append(new_nodes)
        I.append(I_hN)

        if len(I) > 1:
            precisions.append(abs(I[-1] - I[-2]) / (2 ** p - 1))
        N += 1
        printer.task_iter_info(N, h_N[-1], I[-1], precisions[-1], epsilon, nodes[-1])

    return I, precisions, nodes, h_N

from integral_formulas import left_rectangle, trapezoid, simpson
from runge import runge_algorithm
from printer import task_info


def f(x):
    return 4 / (1 + x ** 2)


def second_task(a: float, b: float, epsilon: float):
    task_info("Second task")
    task_info("Left rectangles")
    p_left_rect = 1
    I_left_rect, precisions_left_rect, nodes_left_rect, h_N_left_rect = runge_algorithm(f, a, b, b - a, left_rectangle,
                                                                                        p_left_rect, epsilon)

    task_info("Trapezoid")
    p_trapezoid = 2
    I_trapezoid, precisions_trapezoid, nodes_trapezoid, h_N_trapezoid = runge_algorithm(f, a, b, b - a, trapezoid,
                                                                                        p_trapezoid, epsilon)

    task_info("Simpson")
    p_simpson = 4
    I_simpson, precisions_simpson, nodes_simpson, h_N_simpson = runge_algorithm(f, a, b, b - a, simpson,
                                                                                        p_simpson, epsilon)

    return I_left_rect, I_trapezoid, I_simpson

from math import log
from integral_formulas import left_rectangle
from runge import runge_algorithm
from printer import task_info


def f(x):
    return 1 / (1 - log(x))


def third_task(a: float, b: float, epsilon: float):
    p = 1
    task_info("Third task")
    I2, precisions, nodes, h_N = runge_algorithm(f, a, b, b - a, left_rectangle, p, epsilon)

    return I2

import numpy as np
from math import *
import solution_of_the_stationary_systems.Gaussian_elimination as Gauss
from solution_of_the_stationary_systems.method_of_simple_iteration import get_norm_vector


def f(x):
    return np.array([[sin(x[1][0]) + 2 * x[0][0] - 2],
                     [x[1][0] + cos(x[0][0] - 1) - 0.7]])


def Jacobian(x):
    return np.array([[2, cos(x[1])],
                     [-sin(x[0] - 1), 1]])


def solve(f, jac, x0, eps):
    k = 0
    while True:
        k += 1
        x = x0 + Gauss.solve(jac(x0), -f(x0))
        if get_norm_vector(x - x0) < eps:
            return x, k
        x0 = x


eps = 10 ** -4
x0 = np.array([[1],
               [-0.5]])
x, k = solve(f, Jacobian, x0, eps)
print(x, k)

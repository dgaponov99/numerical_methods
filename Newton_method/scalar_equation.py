from math import *
import numpy as np
import matplotlib.pyplot as plt


def h(x):
    return x ** 3


def g(x):
    return exp(x) - 1


def f(x):
    return h(x) - g(x)


def derivative_f(x):
    return 3 * x ** 2 - exp(x)


def plot(funcs, x):
    n = len(funcs)
    for i in range(n):
        y = []
        for j in x:
            y.append(funcs[i](j))
        plt.plot(x, y)
    plt.axis('equal')
    plt.grid()
    plt.show()


def solve(f, deriv, x0, eps):
    k = 0
    while True:
        k += 1
        x = x0 - f(x0) / deriv(x0)
        if abs(x - x0) < eps:
            return x, k
        x0 = x


def min_ans(ans):
    m = ans[0]
    for i in range(len(ans) - 1):
        if abs(ans[i + 1][0]) < abs(m[0]):
            m = ans[i + 1]
    return m


def search(f, derive, interval, eps):
    x = np.arange(interval[0], interval[1], 100 * eps)
    plot([f], x)
    k = len(x)
    ans = []
    for i in range(k - 1):
        if f(x[i]) * f(x[i + 1]) < 0:
            root, k = solve(f, derive, x[i], eps)
            if abs(root) > eps:
                ans.append([root, x[i], k])
    return min_ans(ans)


eps = 10 ** -4
a = -1
b = 4.6

root = search(f, derivative_f, [a, b], eps)
print('Answer:', root)

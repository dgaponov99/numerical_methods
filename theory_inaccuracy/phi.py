from math import *


# Вычисление кол-ва членов в рядах Маклорена


def fun(x, n):
    for i in range(n + 1):
        print(
            (pi / 2 - 2 * x - 1.05) ** (2 * i) / factorial(2 * i)
        )


# fun(0.01, 4)


def fun2(x, n):
    s = 1 + pi / 2
    for i in range(n + 1):
        s -= (-1) ** i * (((6.4 * x + 1.1) ** (-2 * i - 1)) / (2 * i + 1))
    return s


def fun3(x, n):
    w0 = 2
    w = 0
    phi = fun2(x, 33)
    for i in range(n + 1):
        w = 0.5 * (w0 + phi / w0)
        print(abs(w - w0)/phi)
        w0 = w

fun3(0.06, 4)


fun2(0.06, 33)

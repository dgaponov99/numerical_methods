import numpy as np


def minimize(A, b, eps):
    k = 0
    x = b.copy()
    n = A.shape[0]
    min = np.dot(A, x) + b
    while np.linalg.norm(min) > eps:
        i = k % n
        k += 1
        m = -min[i][0] / A[i][i]
        x[i][0] = x[i][0] + m
        min = np.dot(A, x) + b
    return x, k

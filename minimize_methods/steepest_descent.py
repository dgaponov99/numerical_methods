import numpy as np


def minimize(A, b, eps):
    x = b
    k = 0
    q = np.dot(A, x) + b
    while np.linalg.norm(q) > eps:
        k += 1
        m = -np.dot(q.T, q) / np.dot(np.dot(q.T, A), q)
        x = x + m * q
        q = np.dot(A, x) + b
    return x, k

import numpy as np


def get_good():
    A = np.array([[4., 1., 1.],
                  [1., 6., 1.],
                  [1., 1., 8.]])

    b = np.array([[6.],
                  [8.],
                  [10.]])
    return A, b


def get_bad(n, N, e):
    A1 = np.eye(n)
    A2 = np.ones((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            A1[i][j] = -1
            A2[i][j] = -1

    A = A1 + N * e * A2

    b = -1 * np.ones((n, 1))
    b[n - 1][0] = 1
    return A, b


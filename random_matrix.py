import numpy as np


def get_square_matrix(n):
    return np.random.rand(n, n)


def get_vector(n):
    return np.random.rand(n, 1)


def get_positive_definite_matrix(n):
    while True:
        A = get_square_matrix(n)
        A = np.dot(A, A.T)
        eigvals = np.linalg.eigvals(A)
        if np.all(eigvals > 0):
            return A

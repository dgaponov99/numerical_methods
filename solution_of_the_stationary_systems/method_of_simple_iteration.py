from solution_of_the_stationary_systems.matrix import *


def get_norm(A):
    n = A.shape[0]
    sum = [0] * n
    for i in range(n):
        for j in range(n):
            sum[i] += abs(A[j, i])
    return max(sum)


def get_norm_vector(x):
    n = x.shape[0]
    e = [0] * n
    for i in range(n):
        e[i] = abs(x[i, 0])
    return max(e)


def get_new_view(A, b):
    n = A.shape[0]
    norm = get_norm(A)
    B = (norm * np.eye(n) - A) / norm
    c = b / norm
    return B, c


def solve(A, b, eps):
    B, c = get_new_view(A, b)
    x = c
    k = 0
    while True:
        k += 1
        prev = x
        x = np.add(c, np.dot(B, x))
        if get_norm_vector(x - prev) < eps:
            return x, k


# A, b = get_good()
# print(A)
# print(b)
# x, k = solve(A, b, 10 ** -9)
# print("Answer:")
# print(x)
# print("Iter:")
# print(k)

A, b = get_bad(6, 2, 10 ** -5)
print(A)
print(b)
x, k = solve(A, b, 10 ** -5)
print("Answer:")
print(x)
print("Iter:")
print(k)

from solution_of_the_stationary_systems.matrix import *


def solve(A, b):
    n = A.shape[0]
    T = np.concatenate((A, b), axis=1)
    for i in range(n):
        a = T[i][i]
        for j in range(n + 1):
            T[i, j] /= a
        if i > n - 1:
            break
        for k in range(i + 1, n):
            c = T[k, i]
            for j in range(i, n + 1):
                T[k, j] -= T[i, j] * c

    ans = np.ones((n, 1))
    for i in range(n):
        ans[n - 1 - i, 0] = T[n - 1 - i, n]
        for j in range(i):
            ans[n - 1 - i, 0] -= ans[n - 1 - j, 0] * T[n - 1 - i, n - 1 - j]

    return ans


# A, b = get_bad(5, 2, 5 * 10 ** -7)
# A, b = get_good()
# print(A)
# print(b)
# print(solve(A, b))

import numpy as np

import random_matrix as rm
import minimize_methods.steepest_descent as sd
import solution_of_the_stationary_systems.Gaussian_elimination as gauss
import minimize_methods.coordinate_descent as cd

n = 3
A = rm.get_positive_definite_matrix(n)
b = rm.get_vector(n)
eps = 10 ** -7

print("A = ")
print(A)
print("b = ")
print(b)
print('Искомая точность решения:')
print(eps)
print('\n')


print('-----------------------------------------------------')
print('Точный метод Гаусса')
x_min = gauss.solve(A, -b)
print('Минимум функции:')
print(np.dot(x_min.T, np.dot(A, x_min)) + x_min.T @ b)
print('Решение:')
print(x_min)
print('\n')


print('-----------------------------------------------------')
print('МНГС')
x_minG, k = sd.minimize(A, b, eps)
print('Минимум функции:')
print(np.dot(x_minG.T, np.dot(A, x_minG)) + x_minG.T @ b)
print('Решение:')
print(x_minG)
print('Кол-во итераций:')
print(k)
print('Разница с точным решением:')
print(x_min - x_minG)
print('\n')


print('-----------------------------------------------------')
print('МПС')
x_minC, k = cd.minimize(A, b, eps)
print('Минимум функции:')
print(np.dot(x_minC.T, np.dot(A, x_minC)) + x_minC.T @ b)
print('Решение:')
print(x_minC)
print('Кол-во итераций:')
print(k)
print('Разница с точным решением:')
print(x_min - x_minC)


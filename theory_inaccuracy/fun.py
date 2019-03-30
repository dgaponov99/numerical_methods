from math import *


# Вычисление функции
# z = sqrt(1 + arctg(6.4x+1.1))/sin(2x+1.05)
# с точностью до 10^-6

def fun(x, n, p, k):
    phi = 1 + pi / 2
    for i in range(n + 1):
        phi -= (-1) ** i * (((6.4 * x + 1.1) ** (-2 * i - 1)) / (2 * i + 1))
    # print(phi)

    psi = 0
    for i in range(p + 1):
        psi += (-1) ** i * ((pi / 2 - (2 * x + 1.05)) ** (2 * i)) / factorial(2 * i)
    # print(psi)

    w0 = 2
    w = 0
    for i in range(k + 1):
        w = 0.5 * (w0 + phi / w0)
        w0 = w

    return w / psi


for x in range(10, 65, 5):
    x = x / 100
    print('x =', x)
    z = fun(x, 33, 4, 4)
    za = sqrt(1 + atan(6.4 * x + 1.1)) / sin(2 * x + 1.05)
    print('\tz* =', z, '\n\tz =', za)
    print('\t|z* - z| =', abs(z - za))

from scipy.integrate import *
import numpy as np

# The first integral
def f_x(x):
    return np.exp(-x**2)

print(f"The first integral: {quad(f_x, 0, np.inf)}", f"His numerical value: {np.sqrt(np.pi)/2}\n")

# The second integral
def f(x):
    return 1 / (1 + x**2)

print(f"Yhe second integral: {quad(f, 0, np.inf)}", f"His numerical value: {np.pi/2}\n")

# The third integral
def f(x, y):
    return np.sqrt(1 - x**2 - y**2)

def f2(x):
    return np.sqrt(1 - x**2)

def f1(x):
    return 0

print(f"The double integral: {dblquad(f, -1, 1, f1, f2)}", f"His numerical value: {np.pi/3}\n")

#
# Функция для интегрирования
def integrand(z, y, x):
    return (x * y * z) / (1 + x + y + z)**3

# Пределы интегрирования
def limits_z(y, x):
    return [0, 1 - x - y]

def limits_y(x):
    return [0, 1 - x]

limits_x = [0, 1]

# Вычисление интеграла
result, error = nquad(integrand, [limits_z, limits_y, limits_x])

print(f"Значение интеграла: {result}", (8 * np.log(2)-5)/16)
print(f"Погрешность: {error}")

import matplotlib.pyplot as plt
from numpy import pi
import numpy as np

sigma = 1
myu = 2

x = np.linspace(-4, 7, 100)
x1 = np.random.normal(myu, sigma, 100)

f_x = (1 / (sigma * np.sqrt(2 * pi))) * np.exp(-(x - myu)**2 / (2 * sigma**2))

plt.plot(x, f_x, 'k-', label='f(x)')

plt.hist(x1, 20, density=True, facecolor='b')
plt.axis([-4, 8, 0, 0.5])
plt.grid()
plt.show()
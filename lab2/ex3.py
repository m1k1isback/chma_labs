import matplotlib.pyplot as plt
from numpy import pi
import numpy as np

sigma = 1
myu = 2

x = np.linspace(-4, 7, 100)

f_x = (1 / sigma * np.sqrt(2*pi))*np.exp(-(x-myu)**2/2*sigma**2)
print(f_x)

plt.plot(x, f_x, 'k-', label='f(x)')

# Гистограмма для f_x
plt.hist(f_x, 20, density=True, facecolor='b')
plt.axis([-4.0, 8.0, 0.0, 10])
plt.grid()
plt.show()
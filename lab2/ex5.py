import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

x, y = np.meshgrid(x, y)

x_vec = (x+5) / ((x+5)**2+y**2) - (x-5) / ((x-5)**2+y**2)
y_vec = y / ((x+5)**2+y**2) - y / ((x-5)**2+y**2)

plt.streamplot(x, y, x_vec, y_vec)
plt.scatter([5], [0], s=300, color='b')
plt.scatter([-5], [0], s=300, color='r')
plt.grid(False)
plt.show()
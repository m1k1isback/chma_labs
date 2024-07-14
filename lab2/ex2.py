import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

a = np.arange(0, 2*pi, pi/30)

x_a = np.cos(a) * np.sin(a)
y_a = 1.5*np.cos(a)**2 - 1
p_a = np.cos(a)

# subplot 1
plt.subplot(121)
plt.plot(a, x_a, 'ro-', a, y_a, 'ys-', a, p_a, 'bx-')
plt.grid()

# subplot 2
plt.subplot(122, polar=True)
plt.plot(a, x_a, 'r-', a, y_a, 'y-', a, p_a, 'b-', linewidth=3)
plt.show()


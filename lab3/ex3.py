import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func(y, a):
    return y * a

# subplot 1
plt.subplot(121)
a = np.linspace(-20, 20, 1000)
y0 = 1
y = odeint(func, y0, a)
print(y)
plt.plot(a, y, 'ro-')

# subplot 2
plt.subplot(122)
t = np.linspace(0, 2, 100)
plt.plot(t, np.exp(a[0] * t), 'bo-')

plt.show()




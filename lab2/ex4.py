import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

x = np.linspace(-1.5, 1.5, 100)
y = np.linspace(-1.5, 1.5, 100)

x, y = np.meshgrid(x, y)

z = np.sin(x**2+y**2)

surf = ax.plot_surface(x, y, z, cmap=plt.cm.rainbow, rstride=4, cstride=4)
fig.colorbar(surf, shrink=0.5, aspect=10)
ax.contourf(x,y,z, zdir='z', offset=-1, cmap=plt.cm.rainbow)
plt.show()


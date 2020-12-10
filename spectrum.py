import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-np.pi, np.pi, 0.001)
Y = np.arange(-np.pi/2, np.pi/2, 0.001)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(np.cos(X)**2+np.cos(Y)**2)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
surf = ax.plot_surface(X, Y, -Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# Customize the z axis.
ax.set_zlim(-1.5, 1.5)
ax.zaxis.set_major_locator(LinearLocator(5))
# A StrMethodFormatter is used automatically
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('Spectrum')
plt.xlabel("$k_x$")
plt.ylabel("$k_y$")
plt.yticks([-1.5, -0.5, 0.5, 1.5])
plt.show()
plt.savefig('Spectrum.png', dpi=500)

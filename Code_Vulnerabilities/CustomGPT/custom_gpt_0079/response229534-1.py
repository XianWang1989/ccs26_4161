
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a grid of x and y values
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z values, ensuring to handle potential NaNs
z = np.zeros_like(x)

for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        try:
            z[i, j] = (2*x[i, j]**2 * (np.sqrt(x[i, j]**2 - 4*x[i, j] + y[i, j]**2 + 8) +
                                        np.sqrt(x[i, j]**2 + 4*x[i, j] + y[i, j]**2 + 8)) -
                                        x[i, j]*(y[i, j]**2 - 4) *
                                        (np.sqrt(x[i, j]**2 - 4*x[i, j] + y[i, j]**2 + 8) -
                                         np.sqrt(x[i, j]**2 + 4*x[i, j] + y[i, j]**2 + 8)) -
                                        2*(y[i, j]**2 + 4) +
                                        (np.sqrt(x[i, j]**2 - 4*x[i, j] + y[i, j]**2 + 8) +
                                         np.sqrt(x[i, j]**2 + 4*x[i, j] + y[i, j]**2 + 8)) +
                                        x[i, j]**3 *
                                        (np.sqrt(x[i, j]**2 + 4*x[i, j] + y[i, j]**2 + 8) -
                                         np.sqrt(x[i, j]**2 - 4*x[i, j] + y[i, j]**2 + 8))) /
                                        ((x[i, j]**2 - 4*x[i, j] + y[i, j]**2 + 4) *
                                         np.sqrt(x[i, j]**2 - 4*x[i, j] + y[i, j]**2 + 8) *
                                         (x[i, j]**2 + 4*x[i, j] + y[i, j]**2 + 4) *
                                         np.sqrt(x[i, j]**2 + 4*x[i, j] + y[i, j]**2 + 8)))
        except Exception as e:
            z[i, j] = np.nan  # Set to NaN if an error occurs

# Plot setup
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(-0.1, 0.1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

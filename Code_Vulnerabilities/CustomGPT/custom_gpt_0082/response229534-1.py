
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Create grid data
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z, handle division and possible NaN values
with np.errstate(divide='ignore', invalid='ignore'):
    z = (2*x**2 * (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) -
         x * (y**2 - 4) * (np.sqrt(x**2 - 4*x + y**2 + 8) - np.sqrt(x**2 + 4*x + y**2 + 8)) -
         2*(y**2 + 4) + (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) +
         x**3 * (np.sqrt(x**2 + 4*x + y**2 + 8) - np.sqrt(x**2 - 4*x + y**2 + 8))) / \
        ((x**2 - 4*x + y**2 + 4) * np.sqrt(x**2 - 4*x + y**2 + 8) *
         (x**2 + 4*x + y**2 + 4) * np.sqrt(x**2 + 4*x + y**2 + 8))

# Replace NaNs with zero or any other value
z = np.nan_to_num(z)

# Plot surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-0.1, 0.1)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

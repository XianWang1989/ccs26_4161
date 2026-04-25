
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate the x and y values
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Compute the z values and handle any invalid computations
z = (2 * x**2 * (np.sqrt(x**2 - 4 * x + y**2 + 8) +
     np.sqrt(x**2 + 4 * x + y**2 + 8)) - x * (y**2 - 4) *
     (np.sqrt(x**2 - 4 * x + y**2 + 8) - np.sqrt(x**2 + 4 * x + y**2 + 8)) -
     2 * (y**2 + 4) + (np.sqrt(x**2 - 4 * x + y**2 + 8) + np.sqrt(x**2 + 4 * x + y**2 + 8)) +
     x**3 * (np.sqrt(x**2 + 4 * x + y**2 + 8) - np.sqrt(x**2 - 4 * x + y**2 + 8))) / \
     ((x**2 - 4 * x + y**2 + 4) * np.sqrt(x**2 - 4 * x + y**2 + 8) *
     (x**2 + 4 * x + y**2 + 4) * np.sqrt(x**2 + 4 * x + y**2 + 8))

# Mask invalid values
z = np.ma.masked_invalid(z)

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-0.1, 0.1)

# Customize the z axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar to the plot
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the ranges for x and y
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Define the z function; ensure it's valid across the meshgrid
z = (2 * x**2 * (np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)) + np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0))) -
     x * (y**2 - 4) * (np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)) - np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0))) -
     2 * (y**2 + 4) + (np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)) + np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0))) +
     x**3 * (np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0)) - np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)))) / \
     ((x**2 - 4 * x + y**2 + 4) * np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)) * 
      (x**2 + 4 * x + y**2 + 4) * np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0)))

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-0.1, 0.1)

# Format the z axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

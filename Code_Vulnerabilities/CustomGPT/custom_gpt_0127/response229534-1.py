
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a mesh grid for x and y
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Compute z values safely, using np.clip to avoid issues with complex numbers
z = (2 * x**2 * (np.sqrt(x**2 - 4 * x + y**2 + 8) + np.sqrt(x**2 + 4 * x + y**2 + 8))
     - x * (y**2 - 4) * (np.sqrt(x**2 - 4 * x + y**2 + 8) - np.sqrt(x**2 + 4 * x + y**2 + 8))
     - 2 * (y**2 + 4) + (np.sqrt(x**2 - 4 * x + y**2 + 8) + np.sqrt(x**2 + 4 * x + y**2 + 8))
     + x**3 * (np.sqrt(x**2 + 4 * x + y**2 + 8) - np.sqrt(x**2 - 4 * x + y**2 + 8))
     ) / ((x**2 - 4 * x + y**2 + 4) * np.sqrt(np.clip(x**2 - 4 * x + y**2 + 8, a_min=0, a_max=None))
         * (x**2 + 4 * x + y**2 + 4) * np.sqrt(np.clip(x**2 + 4 * x + y**2 + 8, a_min=0, a_max=None)))

# Create the surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set the z-axis limit
ax.set_zlim(-0.1, 0.1)

# Major ticks on the z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

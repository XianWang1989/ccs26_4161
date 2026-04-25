
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig = plt.figure()
ax = fig.gca(projection='3d')

# Create meshgrid
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Define a function for z
z = (2*x**2 * (np.sqrt(x**2 - 4*x + y**2 + 8)) - 2*(y**2 + 4)) / (x**2 + y**2 + 1)

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Set limits
ax.set_zlim(-10, 10)

# Customize ticks
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for the x and y axes
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Define the function for z
z = (2*x**2 * (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) -
     x * (y**2 - 4) * (np.sqrt(x**2 - 4*x + y**2 + 8) - np.sqrt(x**2 + 4*x + y**2 + 8)) -
     2*(y**2 + 4) + 
     (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) + 
     x**3 * (np.sqrt(x**2 + 4*x + y**2 + 8) - np.sqrt(x**2 - 4*x + y**2 + 8))) / (
     (x**2 - 4*x + y**2 + 4) * np.sqrt(x**2 - 4*x + y**2 + 8) *
     (x**2 + 4*x + y**2 + 4) * np.sqrt(x**2 + 4*x + y**2 + 8))

# Plot the surface with the desired properties
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set z limits
ax.set_zlim(np.min(z), np.max(z))

# Customize the z axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar to the plot
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

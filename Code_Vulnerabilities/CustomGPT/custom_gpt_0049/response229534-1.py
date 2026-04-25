
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.gca(projection='3d')

# Create the grid of x and y values
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z values
z = (2 * x**2 * (np.sqrt(x**2 - 4 * x + y**2 + 8) + np.sqrt(x**2 + 4 * x + y**2 + 8)) - 
     x * (y**2 - 4) * (np.sqrt(x**2 - 4 * x + y**2 + 8) - np.sqrt(x**2 + 4 * x + y**2 + 8)) - 
     2 * (y**2 + 4) + (np.sqrt(x**2 - 4 * x + y**2 + 8) + 
     np.sqrt(x**2 + 4 * x + y**2 + 8)) + x**3 * 
     (np.sqrt(x**2 + 4 * x + y**2 + 8) - np.sqrt(x**2 - 4 * x + y**2 + 8))) / 
     ((x**2 - 4 * x + y**2 + 4) * 
     np.sqrt(x**2 - 4 * x + y**2 + 8) * (x**2 + 4 * x + y**2 + 4) * 
     np.sqrt(x**2 + 4 * x + y**2 + 8))

# Ensure z values are within a reasonable range for coloring
z = np.clip(z, -10, 10)  # Adjust this range based on your data

# Create the surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)

# Set the z limits
ax.set_zlim(-10, 10)  # Update as needed

# Set major ticks on the z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar for the surface
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

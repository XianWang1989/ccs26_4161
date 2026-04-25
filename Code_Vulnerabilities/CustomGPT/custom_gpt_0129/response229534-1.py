
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis for a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid of (x,y) values
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Compute z values
z = (2*x**2 * (np.sqrt(x**2 - 4 * x + y**2 + 8) + np.sqrt(x**2 + 4 * x + y**2 + 8))
     - x * (y**2 - 4) * (np.sqrt(x**2 - 4 * x + y**2 + 8) - np.sqrt(x**2 + 4 * x + y**2 + 8))
     - 2 * (y**2 + 4) + (np.sqrt(x**2 - 4 * x + y**2 + 8) + np.sqrt(x**2 + 4 * x + y**2 + 8))
     + x**3 * (np.sqrt(x**2 + 4 * x + y**2 + 8) - np.sqrt(x**2 - 4 * x + y**2 + 8))) / (
     (x**2 - 4 * x + y**2 + 4) * np.sqrt(x**2 - 4 * x + y**2 + 8) * 
     (x**2 + 4 * x + y**2 + 4) * np.sqrt(x**2 + 4 * x + y**2 + 8))

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set limits on z-axis
ax.set_zlim(-1, 1)  # Adjust these limits based on your z values

# Configure z-axis major locator and formatter
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

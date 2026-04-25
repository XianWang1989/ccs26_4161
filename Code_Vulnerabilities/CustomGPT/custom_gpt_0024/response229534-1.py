
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a new figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate grid data
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Sample function to generate z values
z = (2 * x**2 * (np.sqrt(x**2 - 4 * x + y**2 + 8) + 
    np.sqrt(x**2 + 4 * x + y**2 + 8)) - x * (y**2 - 4) * 
    (np.sqrt(x**2 - 4 * x + y**2 + 8) - 
    np.sqrt(x**2 + 4 * x + y**2 + 8)) - 2 * (y**2 + 4) +
    (np.sqrt(x**2 - 4 * x + y**2 + 8) + 
    np.sqrt(x**2 + 4 * x + y**2 + 8)) + 
    x**3 * (np.sqrt(x**2 + 4 * x + y**2 + 8) - 
    np.sqrt(x**2 - 4 * x + y**2 + 8)) / 
    ((x**2 - 4 * x + y**2 + 4) * 
    np.sqrt(x**2 - 4 * x + y**2 + 8) * 
    (x**2 + 4 * x + y**2 + 4) * 
    np.sqrt(x**2 + 4 * x + y**2 + 8))

# Create the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set color limits for better shading
ax.set_zlim(-10, 10)

# Format the z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

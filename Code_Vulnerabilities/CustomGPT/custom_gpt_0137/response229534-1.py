
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create figure and 3D axis
fig = plt.figure()
ax = fig.gca(projection='3d')

# Generate X and Y data
x = y = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(x, y)

# Compute Z values; Adjust the function for better color visibility
z = np.sin(np.sqrt(x**2 + y**2))  # Change this for more variation in heights

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set limits
ax.set_zlim(-1, 1)  # Adjust limits based on Z values

# Format the z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

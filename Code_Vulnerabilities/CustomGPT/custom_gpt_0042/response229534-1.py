
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create the figure
fig = plt.figure()
ax = fig.gca(projection='3d')

# Generate meshgrid
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z values
z = (2*x**2 * (np.sqrt(x**2-4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) -
     x*(y**2 - 4) * (np.sqrt(x**2 - 4*x + y**2 + 8) - np.sqrt(x**2 + 4*x + y**2 + 8)) -
     2*(y**2 + 4) + (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) +
     x**3 * (np.sqrt(x**2 + 4*x + y**2 + 8) - np.sqrt(x**2 - 4*x + y**2 + 8))) / \
     ((x**2 - 4*x + y**2 + 4) * np.sqrt(x**2 - 4*x + y**2 + 8) *
      (x**2 + 4*x + y**2 + 4) * np.sqrt(x**2 + 4*x + y**2 + 8))

# Handle NaN values in z
z = np.nan_to_num(z, nan=0)  # Replace NaNs with zero (or another value as needed)

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set limits for z axis
ax.set_zlim(-0.1, 0.1)

# Format z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

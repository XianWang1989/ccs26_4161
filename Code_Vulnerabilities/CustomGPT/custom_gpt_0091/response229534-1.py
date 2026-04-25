
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Generate grid data
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)

# Define the function with check for invalid values
z = (2*x**2 * (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) -
     x * (y**2 - 4) * (np.sqrt(x**2 - 4*x + y**2 + 8) - np.sqrt(x**2 + 4*x + y**2 + 8)) -
     2 * (y**2 + 4) + (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) +
     x**3 * (np.sqrt(x**2 + 4*x + y**2 + 8) - np.sqrt(x**2 - 4*x + y**2 + 8))) / \
     ((x**2 - 4*x + y**2 + 4) * np.sqrt(x**2 - 4*x + y**2 + 8) *
      (x**2 + 4*x + y**2 + 4) * np.sqrt(x**2 + 4*x + y**2 + 8))

# Replace NaN values with a specific value or mask them
z[np.isnan(z)] = 0  # or use z = np.ma.masked_invalid(z)

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set limits
ax.set_zlim(-0.1, 0.1)

# Customize ticks
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

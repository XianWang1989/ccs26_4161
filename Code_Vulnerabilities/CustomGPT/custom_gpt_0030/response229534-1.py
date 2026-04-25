
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for x and y values
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Compute z values, ensuring we avoid invalid calculations
z = np.zeros_like(x)

# Example function; replace with your own calculation, ensuring proper handling of values
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        try:
            # Ensure valid operations to avoid NaNs
            z[i, j] = (2 * x[i, j]**2 * (np.sqrt(x[i, j]**2 - 4 * x[i, j] + y[i, j]**2 + 8) +
                                           np.sqrt(x[i, j]**2 + 4 * x[i, j] + y[i, j]**2 + 8)) -
                                           x[i, j] * (y[i, j]**2 - 4) *
                                           (np.sqrt(x[i, j]**2 - 4 * x[i, j] + y[i, j]**2 + 8) -
                                            np.sqrt(x[i, j]**2 + 4 * x[i, j] + y[i, j]**2 + 8)) -
                                           2 * (y[i, j]**2 + 4) +
                                           (np.sqrt(x[i, j]**2 - 4 * x[i, j] + y[i, j]**2 + 8) +
                                            np.sqrt(x[i, j]**2 + 4 * x[i, j] + y[i, j]**2 + 8)) +
                                           x[i, j]**3 * 
                                           (np.sqrt(x[i, j]**2 + 4 * x[i, j] + y[i, j]**2 + 8) -
                                            np.sqrt(x[i, j]**2 - 4 * x[i, j] + y[i, j]**2 + 8))) /
                                          ((x[i, j]**2 - 4 * x[i, j] + y[i, j]**2 + 4) *
                                           np.sqrt(x[i, j]**2 - 4 * x[i, j] + y[i, j]**2 + 8) *
                                           (x[i, j]**2 + 4 * x[i, j] + y[i, j]**2 + 4) *
                                           np.sqrt(x[i, j]**2 + 4 * x[i, j] + y[i, j]**2 + 8)))
        except (ValueError, ZeroDivisionError):
            z[i, j] = np.nan  # Handle invalid cases

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set z-axis limits
ax.set_zlim(-0.1, 0.1)

# Customize z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

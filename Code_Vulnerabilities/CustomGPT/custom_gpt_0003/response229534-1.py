
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig = plt.figure()
ax = fig.gca(projection='3d')

# Define the range for x and y
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Safe computation to avoid invalid values
z = np.zeros_like(x)  # Initialize z with zeros

# Calculate z values, ensuring to check for valid entries
with np.errstate(invalid='ignore', divide='ignore'):
    sqrt_term1 = np.sqrt(x**2 - 4*x + y**2 + 8)
    sqrt_term2 = np.sqrt(x**2 + 4*x + y**2 + 8)

    valid_mask = (sqrt_term1 >= 0) & (sqrt_term2 >= 0) & ((x**2 - 4 * x + y**2 + 4) != 0) & ((x**2 + 4 * x + y**2 + 4) != 0)

    z[valid_mask] = (2 * x[valid_mask]**2 * (sqrt_term1[valid_mask] + sqrt_term2[valid_mask]) - 
                     x[valid_mask] * (y[valid_mask]**2 - 4) * (sqrt_term1[valid_mask] - sqrt_term2[valid_mask]) -
                     2 * (y[valid_mask]**2 + 4) +
                     (sqrt_term1[valid_mask] + sqrt_term2[valid_mask]) + 
                     x[valid_mask]**3 * (sqrt_term2[valid_mask] - sqrt_term1[valid_mask])) / (
                     (x[valid_mask]**2 - 4*x[valid_mask] + y[valid_mask]**2 + 4) * 
                     sqrt_term1[valid_mask] * 
                     (x[valid_mask]**2 + 4*x[valid_mask] + y[valid_mask]**2 + 4) * 
                     sqrt_term2[valid_mask])

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set z limits
ax.set_zlim(-0.1, 0.1)

# Configure axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Display the plot
plt.show()

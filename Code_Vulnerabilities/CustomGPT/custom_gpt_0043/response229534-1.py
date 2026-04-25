
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z values. Be sure to handle divisions that could lead to NaN.
z = (2*x**2 * (np.sqrt(np.maximum(x**2 - 4*x + y**2 + 8, 0)) + np.sqrt(np.maximum(x**2 + 4*x + y**2 + 8, 0))) -
     x * (y**2 - 4) * (np.sqrt(np.maximum(x**2 - 4*x + y**2 + 8, 0)) - np.sqrt(np.maximum(x**2 + 4*x + y**2 + 8, 0))) -
     2 * (y**2 + 4) + (np.sqrt(np.maximum(x**2 - 4*x + y**2 + 8, 0)) + np.sqrt(np.maximum(x**2 + 4*x + y**2 + 8, 0))) + 
     x**3 * (np.sqrt(np.maximum(x**2 + 4*x + y**2 + 8, 0)) - np.sqrt(np.maximum(x**2 - 4*x + y**2 + 8, 0))) /
     ((x**2 - 4 * x + y**2 + 4) * np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)) * 
     (x**2 + 4 * x + y**2 + 4) * np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0))))

# Replace NaN values with zeros or any other static value
z = np.nan_to_num(z)

# Generate the surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Set z limits
ax.set_zlim(-0.1, 0.1)

# Formatting the z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar for reference
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

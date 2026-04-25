
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the meshgrid
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z values and handle potential NaN values
z = (2*x**2 *(np.sqrt(x**2-4 * x+y**2+8)+ np.sqrt(x**2+4 * x+y**2+8)) -
     x*(y**2-4)*(np.sqrt(x**2-4 * x+y**2+8) - np.sqrt(x**2+4 * x+y**2+8)) -
     2*(y**2+4) + (np.sqrt(x**2-4 * x+y**2+8) + np.sqrt(x**2+4 * x+y**2+8)) +
     x**3 * (np.sqrt(x**2+4 * x+y**2+8) - np.sqrt(x**2-4 * x+y**2+8))) / \
    ((x**2-4 * x+y**2+4) * np.sqrt(x**2-4 * x+y**2+8) *
     (x**2+4 * x+y**2+4) * np.sqrt(x**2+4 * x+y**2+8))

# Replace NaN values in z with a constant (e.g., 0)
z = np.nan_to_num(z, nan=0.0)  # You can also choose to use z = np.nan_to_num(z) with specific value

# Create the surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-0.1, 0.1)

# Format the z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

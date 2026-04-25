
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Define the function for z
z = (2*x**2 *(np.sqrt(x**2 - 4 * x + y**2 + 8) + np.sqrt(x**2 + 4 * x + y**2 + 8)) 
     - x*(y**2 - 4)*(np.sqrt(x**2 - 4 * x + y**2 + 8) - np.sqrt(x**2 + 4 * x + y**2 + 8))
     - 2 * (y**2 + 4) + (np.sqrt(x**2 - 4 * x + y**2 + 8) + np.sqrt(x**2 + 4 * x + y**2 + 8))
     + x**3 * (np.sqrt(x**2 + 4 * x + y**2 + 8) - np.sqrt(x**2 - 4 * x + y**2 + 8))
     / ((x**2 - 4 * x + y**2 + 4) * np.sqrt(x**2 - 4 * x + y**2 + 8) 
     * (x**2 + 4 * x + y**2 + 4) * np.sqrt(x**2 + 4 * x + y**2 + 8)))

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set z limits
ax.set_zlim(-10, 10)  # Adjust based on your z data

# Color bar for reference
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

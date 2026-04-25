
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Create a grid of points
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Simple z function to visualize
z = np.sin(np.sqrt(x**2 + y**2))

# Create a 3D figure
fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, 
                       linewidth=0, antialiased=False)

# Set limits and format
ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f')) 

# Add color bar for reference
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Define the range of x and y
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Modify the function for z to ensure more variation
z = np.sin(np.sqrt(x**2 + y**2))

# Create the surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set z limits if necessary
ax.set_zlim(-1, 1)

# Format tick labels
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar for the surface
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

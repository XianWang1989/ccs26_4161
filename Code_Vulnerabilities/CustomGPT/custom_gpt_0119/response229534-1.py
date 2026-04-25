
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure()
ax = fig.gca(projection='3d')

# Create grid
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Define a simpler z function
z = np.sin(np.sqrt(x**2 + y**2))

# Create surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set z limits
ax.set_zlim(-1, 1)

# Customize z axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show plot
plt.show()

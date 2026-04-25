
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a new figure
fig = plt.figure()
ax = fig.gca(projection='3d')

# Create range for x and y
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Compute z values with a more stable function
z = np.sin(np.sqrt(x**2 + y**2))

# Create the surface plot, with color mapping
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set the z axis limits (adjust these based on your z values)
ax.set_zlim(-1, 1)

# Configure the z axis ticks and labels
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar to indicate the mapping
fig.colorbar(surf, shrink=0.5, aspect=5)

# Display the plot
plt.show()

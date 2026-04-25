
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z values; make sure there is sufficient variation in z
z = np.sin(np.sqrt(x**2 + y**2))  # This provides a good range of z values

# Generate the surface plot with a colormap
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)

# Adjust z limits based on your z calculation
ax.set_zlim(-1, 1)  # Adjust this range depending on your z data

# Set the major locator and formatter for z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar to show the color scale
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

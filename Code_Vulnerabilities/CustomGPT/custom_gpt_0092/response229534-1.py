
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create meshgrid
fig = plt.figure()
ax = fig.gca(projection='3d')
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z values
z = (2*x**2 * (np.sqrt(x**2-4*x+y**2+8) + np.sqrt(x**2+4*x+y**2+8)) 
     - x*(y**2-4)*(np.sqrt(x**2-4*x+y**2+8) - np.sqrt(x**2+4*x+y**2+8)) 
     - 2*(y**2+4) 
     + (np.sqrt(x**2-4*x+y**2+8) + np.sqrt(x**2+4*x+y**2+8)) 
     + x**3 * (np.sqrt(x**2+4*x+y**2+8) - np.sqrt(x**2-4*x+y**2+8))) \
     / ((x**2-4*x+y**2+4) * np.sqrt(x**2-4*x+y**2+8) * (x**2+4*x+y**2+4) * np.sqrt(x**2+4*x+y**2+8))

# Adjust z limits if values are too small
z_min, z_max = np.min(z), np.max(z)
if z_min == z_max:  # Prevent color mapping issues
    z_max += 1e-5

# Create the surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set z limits
ax.set_zlim(z_min, z_max)

# Major locator and formatter for z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

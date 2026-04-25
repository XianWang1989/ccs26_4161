
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.gca(projection='3d')

# Define the grid of x and y values
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Define z using a given function
z = (2*x**2 * (np.sqrt(x**2-4*x+y**2+8) + np.sqrt(x**2+4*x+y**2+8)) 
     - x*(y**2-4) * (np.sqrt(x**2-4*x+y**2+8) - np.sqrt(x**2+4*x+y**2+8)) 
     - 2*(y**2+4) 
     + (np.sqrt(x**2-4*x+y**2+8) + np.sqrt(x**2+4*x+y**2+8)) 
     + x**3 * (np.sqrt(x**2+4*x+y**2+8) - np.sqrt(x**2-4*x+y**2+8))
     ) / ((x**2-4*x+y**2+4) * np.sqrt(x**2-4*x+y**2+8) 
          * (x**2+4*x+y**2+4) * np.sqrt(x**2+4*x+y**2+8))

# Remove any potential divide by zero issues
z = np.nan_to_num(z)

# Create the surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Update z-limits dynamically based on the calculated z-values
ax.set_zlim(np.min(z), np.max(z))

# Set z-axis ticks
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

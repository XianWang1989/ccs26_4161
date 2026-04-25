
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Create a meshgrid for x and y
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Compute z values with more variation
z = (2*x**2 * (np.sqrt(x**2-4*x+y**2+8) + np.sqrt(x**2+4*x+y**2+8)) - 
     x*(y**2-4)*(np.sqrt(x**2-4*x+y**2+8) - np.sqrt(x**2+4*x+y**2+8)) - 
     2*(y**2+4) + (np.sqrt(x**2-4*x+y**2+8) + np.sqrt(x**2+4*x+y**2+8)) + 
     x**3 * (np.sqrt(x**2+4*x+y**2+8) - np.sqrt(x**2-4*x+y**2+8))) / (
     (x**2-4*x+y**2+4) * np.sqrt(x**2-4*x+y**2+8) * (x**2+4*x+y**2+4) * np.sqrt(x**2+4*x+y**2+8))

# Create the figure and axis
fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Modify z-axis limits to enhance visibility
ax.set_zlim(z.min(), z.max())

# Customize z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar to show the mapping of colors to heights
fig.colorbar(surf, shrink=0.5, aspect=5)

# Display the plot
plt.show()


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Prepare data
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z values with handling for divisions by zero or invalid operations
z = (2 * x**2 * (np.sqrt(np.maximum(x**2 - 4*x + y**2 + 8, 0)) + 
      np.sqrt(np.maximum(x**2 + 4*x + y**2 + 8, 0))) -
      x * (y**2 - 4) * (np.sqrt(np.maximum(x**2 - 4*x + y**2 + 8, 0)) - 
      np.sqrt(np.maximum(x**2 + 4*x + y**2 + 8, 0))) - 
      2 * (y**2 + 4) +
      (np.sqrt(np.maximum(x**2 - 4*x + y**2 + 8, 0)) +
      np.sqrt(np.maximum(x**2 + 4*x + y**2 + 8, 0))) +
      x**3 * (np.sqrt(np.maximum(x**2 + 4*x + y**2 + 8, 0)) - 
      np.sqrt(np.maximum(x**2 - 4*x + y**2 + 8, 0)))) / (
      (x**2 - 4*x + y**2 + 4) * 
      np.sqrt(np.maximum(x**2 - 4*x + y**2 + 8, 0)) *
      (x**2 + 4*x + y**2 + 4) * 
      np.sqrt(np.maximum(x**2 + 4*x + y**2 + 8, 0)))

# Mask NaN values for plotting
z = np.where(np.isnan(z), 0, z)

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-0.1, 0.1)

# Formatting
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show plot
plt.show()

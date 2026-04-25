
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Adjusted calculation for z to ensure values cover a broader range
z = (2 * x**2 * (np.sqrt(x**2 - 4 * x + y**2 + 8) + 
     np.sqrt(x**2 + 4 * x + y**2 + 8)) - x * (y**2 - 4) *
     (np.sqrt(x**2 - 4 * x + y**2 + 8) - 
     np.sqrt(x**2 + 4 * x + y**2 + 8)) - 
     2 * (y**2 + 4) + 
     (np.sqrt(x**2 - 4 * x + y**2 + 8) + 
     np.sqrt(x**2 + 4 * x + y**2 + 8)) + 
     x**3 * (np.sqrt(x**2 + 4 * x + y**2 + 8) - 
     np.sqrt(x**2 - 4 * x + y**2 + 8))) / 
     ((x**2 - 4 * x + y**2 + 4) * 
     np.sqrt(x**2 - 4 * x + y**2 + 8) * 
     (x**2 + 4 * x + y**2 + 4) * 
     np.sqrt(x**2 + 4 * x + y**2 + 8)))

# Use the proper color mapping
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)

# Set z limits based on observed z values
ax.set_zlim(np.min(z), np.max(z))

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar to show the color mapping
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

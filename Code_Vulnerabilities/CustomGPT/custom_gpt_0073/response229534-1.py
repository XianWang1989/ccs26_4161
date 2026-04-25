
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the meshgrid
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)

# Calculate Z values safely, ensuring no NaNs
z = np.nan_to_num((2*x**2 * (np.sqrt(x**2 - 4*x + y**2 + 8) + 
     np.sqrt(x**2 + 4*x + y**2 + 8)) - x*(y**2 - 4) *
     (np.sqrt(x**2 - 4*x + y**2 + 8) - np.sqrt(x**2 + 4*x + y**2 + 8)) - 
     2*(y**2 + 4) + (np.sqrt(x**2 - 4*x + y**2 + 8) + 
     np.sqrt(x**2 + 4*x + y**2 + 8)) + x**3 * 
     (np.sqrt(x**2 + 4*x + y**2 + 8) - np.sqrt(x**2 - 4*x + y**2 + 8))) /
    ((x**2 - 4*x + y**2 + 4) * 
    np.sqrt(x**2 - 4*x + y**2 + 8) * 
    (x**2 + 4*x + y**2 + 4) * 
    np.sqrt(x**2 + 4*x + y**2 + 8)))

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

ax.set_zlim(-0.1, 0.1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

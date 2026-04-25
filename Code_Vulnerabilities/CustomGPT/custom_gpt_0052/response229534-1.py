
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create meshgrid
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z values, ensuring there are no NaNs
def calculate_z(x, y):
    with np.errstate(divide='ignore', invalid='ignore'):  # Ignore warnings for division by zero
        z = (2*x**2 * (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) -
             x * (y**2 - 4) * (np.sqrt(x**2 - 4*x + y**2 + 8) - np.sqrt(x**2 + 4*x + y**2 + 8)) -
             2 * (y**2 + 4) + (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) +
             x**3 * (np.sqrt(x**2 + 4*x + y**2 + 8) - np.sqrt(x**2 - 4*x + y**2 + 8))) / (
             (x**2 - 4*x + y**2 + 4) * np.sqrt(x**2 - 4*x + y**2 + 8) *
             (x**2 + 4*x + y**2 + 4) * np.sqrt(x**2 + 4*x + y**2 + 8))

        z = np.nan_to_num(z)  # Avoid NaN values
        return z

z = calculate_z(x, y)

# Create surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Set limits for z-axis
ax.set_zlim(-0.1, 0.1)

# Customize z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show plot
plt.show()

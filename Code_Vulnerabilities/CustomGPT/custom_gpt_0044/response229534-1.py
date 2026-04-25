
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Prepare the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate the data
x = np.linspace(-10, 10, 200)
y = np.linspace(-10, 10, 200)
x, y = np.meshgrid(x, y)

# Calculate z, ensuring we handle any potential warnings from invalid operations
z = np.zeros_like(x)

# Mask invalid values to avoid issues
with np.errstate(invalid='ignore', divide='ignore'):
    temp = (2 * x**2 * (np.sqrt(x**2 - 4 * x + y**2 + 8) + 
            np.sqrt(x**2 + 4 * x + y**2 + 8)) - 
            x * (y**2 - 4) * (np.sqrt(x**2 - 4 * x + y**2 + 8) - 
            np.sqrt(x**2 + 4 * x + y**2 + 8)) - 2 * (y**2 + 4) + 
            (np.sqrt(x**2 - 4 * x + y**2 + 8) + 
            np.sqrt(x**2 + 4 * x + y**2 + 8)) + 
            x**3 * (np.sqrt(x**2 + 4 * x + y**2 + 8) - 
            np.sqrt(x**2 - 4 * x + y**2 + 8))) / (
            (x**2 - 4 * x + y**2 + 4) * 
            np.sqrt(x**2 - 4 * x + y**2 + 8) * 
            (x**2 + 4 * x + y**2 + 4) * 
            np.sqrt(x**2 + 4 * x + y**2 + 8))

    z = np.nan_to_num(temp)  # Convert NaNs to 0 and Infs to large finite numbers

# Create the surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set z limits
ax.set_zlim(-0.1, 0.1)

# Customize the z-axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

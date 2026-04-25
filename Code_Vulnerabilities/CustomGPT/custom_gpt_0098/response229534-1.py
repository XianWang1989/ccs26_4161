
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid of x and y values
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Define z values (make sure z has varied values)
z = (2*x**2 * (np.sqrt(x**2-4*x+y**2+8) + np.sqrt(x**2+4*x+y**2+8)) - 
    x*(y**2-4)*(np.sqrt(x**2-4*x+y**2+8) - np.sqrt(x**2+4*x+y**2+8)) - 
    2*(y**2+4) + 
    (np.sqrt(x**2-4*x+y**2+8) + np.sqrt(x**2+4*x+y**2+8)) + 
    x**3 * (np.sqrt(x**2+4*x+y**2+8) - np.sqrt(x**2-4*x+y**2+8))) / (
    (x**2-4*x+y**2+4) * np.sqrt(x**2-4*x+y**2+8) *
    (x**2+4*x+y**2+4) * np.sqrt(x**2+4*x+y**2+8))

# Check range of z values
print(f"z min: {np.min(z)}, z max: {np.max(z)}")  # Print min and max of z

# Create the surface plot
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set z limits (adjust based on your data)
ax.set_zlim(np.min(z), np.max(z))

# Format the z axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

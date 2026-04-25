
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Define your z function
z = (2*x**2 * (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) - 
    x*(y**2 - 4) * (np.sqrt(x**2 - 4*x + y**2 + 8) - np.sqrt(x**2 + 4*x + y**2 + 8)) - 
    2*(y**2 + 4) + (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8)) + 
    x**3 * (np.sqrt(x**2 + 4*x + y**2 + 8) - np.sqrt(x**2 - 4*x + y**2 + 8))) / (
    (x**2 - 4*x + y**2 + 4) * np.sqrt(x**2 - 4*x + y**2 + 8) * (x**2 + 4*x + y**2 + 4) * 
    np.sqrt(x**2 + 4*x + y**2 + 8))

# Check for NaN or inf values in z
if np.any(np.isnan(z)) or np.any(np.isinf(z)):
    print("Warning: z contains NaN or inf values.")

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, 
                       linewidth=0, antialiased=False)

# Set z limits thoughtfully
ax.set_zlim(-10, 10)  # Adjust based on the expected range of z-values

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()

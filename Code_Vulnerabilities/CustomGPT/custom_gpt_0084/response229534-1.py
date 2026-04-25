
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z values, handling potential divisions by zero or invalid values
z = np.zeros_like(x)  # Initialize z with zeros

# Compute z, ensuring no invalid values
term1 = 2 * x**2 * (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8))
term2 = x * (y**2 - 4) * (np.sqrt(x**2 - 4*x + y**2 + 8) - np.sqrt(x**2 + 4*x + y**2 + 8))
term3 = -2 * (y**2 + 4)
term4 = (np.sqrt(x**2 - 4*x + y**2 + 8) + np.sqrt(x**2 + 4*x + y**2 + 8))
term5 = x**3 * (np.sqrt(x**2 + 4*x + y**2 + 8) - np.sqrt(x**2 - 4*x + y**2 + 8))

denominator = (x**2 - 4*x + y**2 + 4) * np.sqrt(np.maximum(x**2 - 4*x + y**2 + 8, 0)) * \
              (x**2 + 4*x + y**2 + 4) * np.sqrt(np.maximum(x**2 + 4*x + y**2 + 8, 0))

# Safely compute z, avoiding division by zero
with np.errstate(divide='ignore', invalid='ignore'):
    z = (term1 + term2 + term3 + term4 + term5) / denominator

# Mask invalid z values (if any)
z[denominator == 0] = np.nan

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(-0.1, 0.1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

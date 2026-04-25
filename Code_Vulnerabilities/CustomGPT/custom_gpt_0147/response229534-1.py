
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Calculate z with safeguards against invalid calculations
with np.errstate(divide='ignore', invalid='ignore'):
    sqrt_term1 = np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0))
    sqrt_term2 = np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0))
    denominator = (x**2 - 4 * x + y**2 + 4) * sqrt_term1 * (x**2 + 4 * x + y**2 + 4) * sqrt_term2

    z = np.where(denominator != 0, 
                  (2 * x**2 * (sqrt_term1 - sqrt_term2) - x * (y**2 - 4) * (sqrt_term1 - sqrt_term2) - 2 * (y**2 + 4) + 
                   (sqrt_term1 + sqrt_term2) + x**3 * (sqrt_term2 - sqrt_term1)) / denominator,
                  0)  # Assign 0 where the denominator is 0, or handle differently if needed

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
ax.set_zlim(-0.1, 0.1)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

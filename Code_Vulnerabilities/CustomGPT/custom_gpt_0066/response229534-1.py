
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)

# Define a function and ensure it handles domains preventing NaN and inf values
def my_function(x, y):
    # Replace values that lead to NaN/inf in z calculation
    with np.errstate(divide='ignore', invalid='ignore'):
        z = (2 * x**2 * (np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)) + 
            np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0))) -
            x * (y**2 - 4) * (np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)) -
            np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0))) -
            2 * (y**2 + 4) + 
            (np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)) + 
            np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0))) +
            x**3 * (np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0)) -
            np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)))) / \
            ((x**2 - 4 * x + y**2 + 4) * 
            np.sqrt(np.maximum(x**2 - 4 * x + y**2 + 8, 0)) * 
            (x**2 + 4 * x + y**2 + 4) * 
            np.sqrt(np.maximum(x**2 + 4 * x + y**2 + 8, 0)))

        # Handle any remaining NaNs by replacing with zeros or another value
        z[np.isnan(z)] = 0
        return z

z = my_function(x, y)

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-0.1, 0.1)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

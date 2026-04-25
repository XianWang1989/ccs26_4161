
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# Generate sample data
num_lines = 50
x = np.linspace(0, 10, 100)
y = np.array([np.sin(x + i) + i for i in np.linspace(0, 5, num_lines)])

# Create density data
density, xedges, yedges = np.histogram2d(np.repeat(x, num_lines), y.flatten(), bins=50, density=True)

# Create grid for contour plot
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
zpos = np.zeros_like(xpos)

# Normalize density for coloring
norm = Normalize(vmin=density.min(), vmax=density.max())
colors = plt.cm.viridis(norm(density))

# Plotting lines
plt.figure(figsize=(10, 6))
for i in range(num_lines):
    plt.plot(x, y[i], alpha=0.5)

# Overlaying density contour
contour = plt.contourf(xedges[:-1], yedges[:-1], density, cmap='viridis', alpha=0.3)

plt.colorbar(contour)
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim([0, 10])
plt.ylim([-1, 10])
plt.grid()
plt.show()

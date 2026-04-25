
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct solutions represented as lines
solutions = [
    (np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)) + i) for i in range(5)
]
probabilities = np.linspace(0.1, 1, len(solutions))  # Sample opacities

# Prepare the figure
fig, ax = plt.subplots()

# Normalize the probabilities for opacity
norm = plt.Normalize(probabilities.min(), probabilities.max())
rgba_colors = plt.cm.viridis(norm(probabilities))

# Create LineCollections
for i, (x, y) in enumerate(solutions):
    segments = np.array([x, y]).T.reshape(-1, 1, 2)
    lc = LineCollection(segments, colors=[rgba_colors[i]], linewidths=2, alpha=probabilities[i])
    ax.add_collection(lc)

# Set limits and aspect
ax.set_xlim(0, 10)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.set_title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter 1')
plt.ylabel('Parameter 2')
plt.grid()

# Show the plot
plt.colorbar(plt.cm.ScalarMappable(cmap='viridis', norm=norm), label='Opacity')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data: distinct lines
line_count = 10
x = np.linspace(0, 10, 100)
lines = []

for i in range(line_count):
    y = np.sin(x + i) + np.random.normal(0, 0.1, x.shape)  # Shifted sine waves
    lines.append(np.column_stack([x, y]))

# Create a LineCollection
line_segments = np.concatenate(lines)
line_segments = line_segments.reshape(-1, 2, 2)

# Create a density-like effect by varying alpha
line_collection = LineCollection(line_segments, linewidths=2, cmap='inferno')

# Set alpha based on density (here just an example based on line count)
alpha_values = np.linspace(0, 1, line_count)
for alpha in alpha_values:
    line_collection.set_array(np.full(line_segments.shape[0], alpha))

fig, ax = plt.subplots()
ax.add_collection(line_collection)

# Set limits and aspect
ax.set_xlim(0, 10)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')

# Add colorbar for alpha representation
sm = plt.cm.ScalarMappable(cmap='inferno', norm=plt.Normalize(0, 1))
sm.set_array([])
plt.colorbar(sm, ax=ax, label='Density (Alpha)')

plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data
num_lines = 5
x = np.linspace(0, 10, 100)
lines = [np.column_stack((x, np.sin(x + i))) for i in np.linspace(0, 2 * np.pi, num_lines)]
probabilities = np.random.rand(num_lines)

# Create LineCollection
segments = np.array(lines)
line_collection = LineCollection(segments, linewidths=2, cmap='viridis', alpha=0.5)

# Normalize probabilities for coloring
norm = plt.Normalize(probabilities.min(), probabilities.max())
line_collection.set_array(probabilities)

# Create the plot
fig, ax = plt.subplots()
ax.add_collection(line_collection)
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
plt.colorbar(line_collection, ax=ax, label='Probability')
ax.set_title('2D Density Plot with Distinct Lines')
plt.grid()
plt.show()

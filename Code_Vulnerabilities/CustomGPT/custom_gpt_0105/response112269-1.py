
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct solutions as lines in 2D space
np.random.seed(0)
n_lines = 10
x = np.linspace(0, 10, 100)
y_lines = [np.sin(x + i) + np.random.normal(0, 0.1, x.shape) for i in range(n_lines)]
probabilities = np.random.rand(n_lines)  # Randomly assign probabilities

# Create a LineCollection with alpha based on probabilities
segments = [np.column_stack([x, y]) for y in y_lines]
line_segments = LineCollection(segments, cmap='viridis', alpha=0.5,
                               array=probabilities, linewidths=2)

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.add_collection(line_segments)
ax.autoscale_view()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-2, 2)
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.colorbar(line_segments, label='Probability')
plt.show()

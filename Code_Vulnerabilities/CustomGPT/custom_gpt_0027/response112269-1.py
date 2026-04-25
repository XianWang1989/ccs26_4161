
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample parameter space data
num_lines = 100
x = np.linspace(0, 10, 100)
lines = []  # List to hold line segments
probabilities = np.random.rand(num_lines)  # Random probabilities for opacity

for i in range(num_lines):
    # For example: y = mx + b with random slope and intercept
    m = np.random.rand() * 2 - 1  # Random slope
    b = np.random.rand() * 10      # Random intercept
    y = m * x + b
    lines.append(np.column_stack((x, y)))

# Create a LineCollection
line_segments = LineCollection(lines, linewidths=1, cmap='viridis', alpha=0)
for i, line in enumerate(line_segments.get_segments()):
    line_segments.set_array(np.array([probabilities[i]]))  # Set color based on probability
    line_segments.set_alpha(probabilities[i])  # Set opacity based on probability

fig, ax = plt.subplots()
ax.add_collection(line_segments)
ax.autoscale_view()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.colorbar(line_segments, ax=ax, label='Probability')
plt.title('2D Density Plot of Distinct Solutions')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid()
plt.show()

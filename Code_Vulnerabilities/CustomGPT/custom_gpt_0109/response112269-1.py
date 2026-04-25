
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate some sample line data
num_lines = 100
x = np.linspace(0, 10, 100)
lines = []

# Create lines with distinct solutions
for i in range(num_lines):
    y = np.sin(x + i * 0.1) + np.random.normal(scale=0.1, size=x.shape)
    lines.append(np.column_stack((x, y)))

# Create a LineCollection
line_segments = np.array(lines)
line_segments = np.concatenate(line_segments, axis=0)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
lc = LineCollection(line_segments.reshape(-1, 2, 2), linewidths=1, colors='blue', alpha=0.5)

# Add the LineCollection to the plot
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.show()

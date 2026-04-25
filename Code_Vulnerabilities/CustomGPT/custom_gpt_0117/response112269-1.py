
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generating sample data
num_lines = 50
x = np.linspace(0, 10, 100)

# Create lines with varying probabilities
lines = []
for i in range(num_lines):
    # Each line can be parameterized differently
    y = np.sin(x + i * np.pi / num_lines) + np.random.normal(scale=0.1, size=x.shape)
    lines.append(np.column_stack([x, y]))

# Create a LineCollection object
line_segments = LineCollection(lines, cmap='viridis', alpha=0.5, linewidth=2)

# Create a new figure
fig, ax = plt.subplots()

# Add LineCollection to the axes
ax.add_collection(line_segments)

# Set limits and labels
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-2, 2)
ax.set_title("2D Density Plot with Distinct Lines")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Show the plot
plt.colorbar(line_segments, ax=ax, label='Probability Density')
plt.show()

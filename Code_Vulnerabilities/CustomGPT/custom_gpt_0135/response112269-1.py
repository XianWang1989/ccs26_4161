
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct lines, each defined by a start and end point
lines = [
    [(0, 0), (1, 2)],
    [(0, 1), (1, 3)],
    [(0, 2), (1, 1)],
    [(0.5, 0), (1.5, 2)],
]

# Corresponding probabilities for each line
probabilities = [0.1, 0.5, 0.8, 0.3]

# Create a list of line segments and their corresponding colors
line_segments = []
colors = []
for line, prob in zip(lines, probabilities):
    line_segments.append(line)
    colors.append((0, 0, 0, prob))  # RGB with alpha set to probability

# Create LineCollection
lc = LineCollection(line_segments, colors=colors, linewidths=2)

# Set up the plot
fig, ax = plt.subplots()
ax.add_collection(lc)

# Set limits and aspect
ax.set_xlim(-0.5, 2)
ax.set_ylim(-0.5, 4)
ax.set_aspect('equal')

# Add grid and labels
ax.grid()
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.show()

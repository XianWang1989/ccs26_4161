
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Example data: distinct lines in the parameter space along with corresponding probabilities
lines = [
    np.array([[0, 0], [1, 2]]),  # Line 1
    np.array([[0, 1], [2, 0]]),  # Line 2
    np.array([[0, 2], [1, 0]]),  # Line 3
]

# Probabilities corresponding to each line
probabilities = [0.3, 0.5, 0.7]

# Create a figure and an axis
fig, ax = plt.subplots()

# Create a list to store the segments and their corresponding colors
segments = []
colors = []

# Create line segments and colors with their respective opacities
for line, prob in zip(lines, probabilities):
    segments.append(line)
    colors.append((0, 0, 0, prob))  # RGBA: black with varying opacities

# Create a LineCollection from the segments
line_segments = LineCollection(segments, colors=colors, linewidths=2)
ax.add_collection(line_segments)

# Set limits and labels
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')

# Show the plot
plt.show()

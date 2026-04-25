
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: list of lines (each defined by start and end points)
lines = [
    np.array([[0, 0], [1, 1]]),
    np.array([[0, 1], [1, 0]]),
    np.array([[0, 0], [0.5, 0.5], [1, 1]])
]

# Corresponding probabilities for each line
probabilities = [0.2, 0.5, 0.8]

# Create a figure and axis
fig, ax = plt.subplots()

# Create a LineCollection
for line, prob in zip(lines, probabilities):
    segments = np.array([line])
    line_collection = LineCollection(segments, linewidths=2, linestyle='-', alpha=prob)
    ax.add_collection(line_collection)

# Set limits
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)

# Adding a grid for reference
ax.grid(True)

# Title and labels
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Show the plot
plt.show()

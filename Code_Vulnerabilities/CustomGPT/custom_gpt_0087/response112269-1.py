
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Example data: each line represented by start and end points
lines = [
    np.array([[1, 2], [4, 5]]),
    np.array([[1, 3], [3, 6]]),
    np.array([[2, 1], [5, 3]])
]

# Probabilities for each line (for opacity)
probabilities = [0.5, 0.7, 0.9]

# Create figure and axis
fig, ax = plt.subplots()

# Create a list of line segments and their opacity
segments = []
colors = []
for line, prob in zip(lines, probabilities):
    segments.append(line)
    colors.append((0, 0, 0, prob))  # RGBA with varying alpha

# Create a LineCollection
lc = LineCollection(segments, linewidths=2, colors=colors)
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 6)
ax.set_ylim(0, 7)
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')
ax.set_title('Density Plot with Distinct Lines')

# Show plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Create sample data
# Example: line segments (x1, y1) to (x2, y2) and corresponding probabilities
lines = [
    ((0, 1), (1, 3), 0.8),
    ((1, 2), (2, 4), 0.5),
    ((2, 0), (3, 3), 0.9),
]

# Prepare the data for LineCollection
segments = []
colors = []
for (x1, y1), (x2, y2), prob in lines:
    segments.append([(x1, y1), (x2, y2)])
    colors.append((0, 0, 0, prob))  # RGBA with varying opacity

# Create a LineCollection
lc = LineCollection(segments, colors=colors, linewidths=2)

# Create the plot
fig, ax = plt.subplots()
ax.add_collection(lc)

# Set limits
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 5)

# Add grid and labels
plt.grid()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Density Plot with Distinct Lines')

plt.show()

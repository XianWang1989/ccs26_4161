
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

# Example data: list of (x, y) coordinates and their associated probabilities
lines = [
    (np.array([0, 1]), np.array([0, 2]), 0.8),
    (np.array([0, 1]), np.array([1, 1.5]), 0.5),
    (np.array([1, 2]), np.array([0, 1]), 0.3),
]

# Create a figure
fig, ax = plt.subplots()

# Prepare segments and colors based on probability
segments = []
colors = []

for x, y, prob in lines:
    segment = np.array([x, y]).T.reshape(-1, 1, 2)
    segments.append(segment)

    # Color: 0.0 (transparent) to 1.0 (opaque)
    color = (0, 0, 0, prob)  # RGBA format
    colors.append(color)

# Combine line segments and colors
line_segments = np.concatenate(segments)
line_colors = [color for color in colors for _ in range(len(x))]  # Repeat for each segment

# Create a LineCollection
lc = LineCollection(line_segments, colors=line_colors, linewidths=2)

# Add to the axes
ax.add_collection(lc)

# Set limits and aspect
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 2.5)
ax.set_aspect('equal')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Density Plot with Distinct Lines')
plt.grid()
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct lines in parameter space with associated probabilities
lines = [
    np.array([[0, 0], [2, 2]]),
    np.array([[0, 2], [2, 0]]),
    np.array([[1, 0], [1, 2]])
]

# Define corresponding probabilities for line opacities
probabilities = [0.2, 0.5, 0.8]

# Create a figure and axis
fig, ax = plt.subplots()

# Create a LineCollection
line_segments = [lines[i] for i in range(len(lines))]
line_collection = LineCollection(line_segments, linewidths=2)

# Set color based on probability
colors = plt.cm.viridis(np.array(probabilities) / max(probabilities))  # Normalize for color mapping
line_collection.set_color(colors)

# Add LineCollection to the axes
ax.add_collection(line_collection)

# Set limits and labels
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 3)
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.set_title('2D Density Plot with Distinct Lines')

# Show grid
ax.grid()

# Show plot
plt.show()

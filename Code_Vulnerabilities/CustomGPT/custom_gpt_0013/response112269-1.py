
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Example data: lines represented as (x, y) pairs and their corresponding probabilities
lines = [
    (np.array([0, 1]), np.array([0, 1]), 0.8),  # Line 1 with probability 0.8
    (np.array([0, 1]), np.array([1, 0]), 0.6),  # Line 2 with probability 0.6
    (np.array([0.5, 1]), np.array([0, 1]), 0.9),  # Line 3 with probability 0.9
]

# Create a figure and axis
fig, ax = plt.subplots()

# Prepare line segments and their probabilities
segments = []
probabilities = []
for x1, y1, prob in lines:
    segments.append(np.column_stack([x1, y1]))
    probabilities.append(prob)

# Create a LineCollection
lc = LineCollection(segments, linewidths=2, cmap='viridis',
                    alpha=0,  # Start with transparent lines
                    array=np.array(probabilities),  # Set probabilities
                    norm=plt.Normalize(0, 1))

# Add LineCollection to the axes
line_collection = ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Density Plot with Distinct Lines")
ax.set_xlabel("Parameter 1")
ax.set_ylabel("Parameter 2")

# Add a colorbar to represent probabilities
cbar = plt.colorbar(line_collection, ax=ax)
cbar.set_label('Probability')

# Draw with adjusted alpha based on probabilities
for i, (x, y, prob) in enumerate(lines):
    ax.plot(x, y, alpha=prob/1.0, linewidth=2)

plt.show()

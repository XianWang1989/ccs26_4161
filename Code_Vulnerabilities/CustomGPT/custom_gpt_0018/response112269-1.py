
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: Define lines with their corresponding probabilities
lines = [
    ([[0, 0], [1, 1]], 0.2),  # Line from (0,0) to (1,1) with a probability of 0.2
    ([[0, 1], [1, 0]], 0.5),  # Line from (0,1) to (1,0) with a probability of 0.5
    ([[0.5, 0], [0, 1]], 0.6),  # Line from (0.5,0) to (0,1) with a probability of 0.6
]

# Prepare the data for LineCollection
segments = []
alphas = []

for line, prob in lines:
    segments.append(line)           # Add line segment coordinates
    alphas.append(prob)             # Add the corresponding probability

# Create a LineCollection with the segments and set the color (black) with varying alpha
line_collection = LineCollection(segments, colors='black', linewidths=2, alpha=0)
for i, alpha in enumerate(alphas):
    line_collection.set_alpha(alpha)  # Set alpha for each line based on its probability

# Plot using Matplotlib
fig, ax = plt.subplots()
ax.add_collection(line_collection)
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter 1')
plt.ylabel('Parameter 2')
plt.grid(False)

plt.show()

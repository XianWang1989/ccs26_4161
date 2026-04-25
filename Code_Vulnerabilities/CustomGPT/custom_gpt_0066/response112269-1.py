
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Example data: distinct lines in parameter space with probabilities
lines = [np.array([[0, 0], [1, 1]]), np.array([[0, 1], [1, 0]])]
probabilities = [0.8, 0.5]  # Corresponding probabilities

# Create a LineCollection
line_segments = [line for line in lines]
colors = [plt.cm.viridis(prob) for prob in probabilities]  # Use colormap for colors
collection = LineCollection(line_segments, colors=colors, linewidths=2)

# Plotting
fig, ax = plt.subplots()
ax.add_collection(collection)

# Set limits
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')

# Add grid and labels
ax.grid(True)
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')

plt.colorbar(collection, ax=ax, label='Probability')
plt.show()

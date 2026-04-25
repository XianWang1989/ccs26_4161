
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct lines in parameter space
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1)

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2)

# Create a list of line segments for LineCollection
lines = [np.column_stack([x1, y1]), np.column_stack([x2, y2])]
segments = np.concatenate(lines)

# Create an array for the probabilities (opacity) of each line
probabilities = [0.5, 0.8]  # Example probabilities for each line

# Create the LineCollection
lc = LineCollection(segments.reshape(-1, 2, 2), linewidths=2, cmap='viridis', alpha=0)

# Normalize probabilities for opacity
norm = plt.Normalize(0, 1)
lc.set_array(np.concatenate([np.full(len(y1), p) for p in probabilities]))
lc.set_clim(0, 1)
lc.set_alpha(1)

# Create the plot
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale_view()
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
plt.colorbar(lc, label='Opacity based on probability')

plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

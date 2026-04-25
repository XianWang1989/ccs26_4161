
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct solutions forming lines (x1, y1) and (x2, y2) 
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + np.random.normal(scale=0.1, size=x1.shape)  # Line 1

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) + np.random.normal(scale=0.1, size=x2.shape)  # Line 2

# Combine the data into a set of segments for LineCollection
points1 = np.array([x1, y1]).T.reshape(-1, 1, 2)
points2 = np.array([x2, y2]).T.reshape(-1, 1, 2)

# Create a LineCollection
segments = np.concatenate([points1, points2])
lc = LineCollection(segments, linewidths=2, cmap='viridis', alpha=0.5)

# Set the colors based on line probability (or any other metric)
lc.set_array(np.concatenate([np.full(y1.shape, 0.7), np.full(y2.shape, 0.3)]))  # Example probabilities
lc.set_clim(0, 1)

# Create the plot
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale_view()
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title('Density Plot of Distinct Solutions')
ax.set_xlabel('Parameter Space X-axis')
ax.set_ylabel('Parameter Space Y-axis')

# Add a colorbar
plt.colorbar(lc, ax=ax, label='Probability')

plt.show()

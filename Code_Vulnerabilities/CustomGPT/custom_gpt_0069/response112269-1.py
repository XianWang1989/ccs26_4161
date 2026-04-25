
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data for distinct solutions (lines)
num_lines = 10
x = np.linspace(0, 10, 100)
lines = [np.vstack((x, np.sin(x + i)).T for i in range(num_lines)]
probabilities = np.random.rand(num_lines)  # Sample probabilities for each line

# Create a LineCollection with blended colors based on probability
colors = plt.cm.viridis(probabilities / probabilities.max())  # Normalize probabilities
line_segments = np.concatenate(lines)

# Creating LineCollection
lc = LineCollection(line_segments, linewidths=2, colors=colors, linestyle='solid', alpha=0.5)

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.add_collection(lc)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add colorbar for probabilities
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(0, 1))
sm.set_array([])  # Create empty array for color bar
plt.colorbar(sm, ax=ax, label='Probability')

plt.show()

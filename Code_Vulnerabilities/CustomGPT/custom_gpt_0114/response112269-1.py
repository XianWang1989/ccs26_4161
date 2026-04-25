
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: generate several lines in parameter space
num_lines = 10
x = np.linspace(0, 10, 100)
lines = []
probabilities = []

for i in range(num_lines):
    slope = np.random.uniform(-1, 1)
    intercept = np.random.uniform(0, 10)
    line = slope * x + intercept
    lines.append(np.column_stack((x, line)))
    probabilities.append(np.random.rand())  # Random probabilities for opacity

# Create a LineCollection
segments = np.array(lines)
lc = LineCollection(segments, cmap='viridis', linewidths=2)

# Set the colors based on probabilities
lc.set_array(np.array(probabilities))
lc.set_linewidth(2)
lc.set_alpha(0.5)  # Set transparency

# Create the plot
fig, ax = plt.subplots()
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.set_title('2D Density Plot of Distinct Solutions')

# Show colorbar
cbar = plt.colorbar(lc, ax=ax)
cbar.set_label('Probability')

plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data: distinct linear solutions
num_lines = 100
x = np.linspace(0, 10, 100)
lines = []
for i in range(num_lines):
    y = np.sin(x + np.random.uniform(0, 2 * np.pi)) + np.random.normal(0, 0.1, x.shape)
    lines.append(np.array([x, y]).T)

# Create a LineCollection with alpha corresponding to probability
colors = plt.cm.viridis(np.linspace(0, 1, num_lines))
line_segments = [line for line in lines]
lc = LineCollection(line_segments, cmap='viridis', alpha=0.8)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
lc.set_array(np.linspace(0, 1, num_lines))  # Set color map based on index
lc.set_linewidth(2)

# Add LineCollection to the Axes
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title('Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Display the plot
plt.colorbar(lc, ax=ax, orientation='vertical', label='Probability Density')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data
np.random.seed(0)
num_lines = 50
x_values = np.linspace(0, 10, 100)
y_values = [np.sin(x + np.random.uniform(0, 2 * np.pi)) + np.random.normal(0, 0.1, size=x.shape) for _ in range(num_lines)]

# Create a colormap for the opacity based on the number of solutions
probabilities = np.linspace(0.1, 1, num_lines)

# Create a LineCollection of the lines
lines = [np.array([x_values, y]).T for y in y_values]
line_segments = LineCollection(lines, cmap='viridis', alpha=0.5)

# Normalize to get the correct alpha blending
line_segments.set_array(probabilities)
line_segments.set_linewidth(2)

fig, ax = plt.subplots()
ax.add_collection(line_segments)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title('Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Show the plot
plt.colorbar(line_segments, ax=ax, label='Probability')
plt.show()

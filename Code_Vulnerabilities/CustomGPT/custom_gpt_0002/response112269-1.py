
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data for distinct lines
x = np.linspace(0, 10, 100)
solutions = [np.column_stack((x, np.sin(x + i))) for i in np.linspace(0, 2*np.pi, 10)]

# Prepare for LineCollection
lines = np.concatenate(solutions)
line_segments = LineCollection(lines.reshape(-1, 1, 2), linewidths=2)

# Generate density values for blending colors
density = np.random.rand(len(lines))  # Dummy density values; replace with actual ones

# Setup the plot
fig, ax = plt.subplots()
line_segments.set_array(density)
line_segments.set_linewidth(2)
line_segments.set_alpha(0.5)  # Set a fixed opacity for blending

# Add LineCollection to the axes
ax.add_collection(line_segments)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.colorbar(line_segments)
plt.show()

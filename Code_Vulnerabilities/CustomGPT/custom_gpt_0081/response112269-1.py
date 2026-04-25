
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate some distinct lines as sample solutions
num_lines = 10
x = np.linspace(0, 10, 100)  # X-axis values
lines = []

# Creating parallel lines with small variations
for i in range(num_lines):
    y = np.sin(x + i) + np.random.normal(0, 0.1, x.shape)  # Adding slight noise
    lines.append(np.column_stack((x, y)))

# Create a LineCollection from the list of lines
line_segments = np.array(lines)
line_segments = np.concatenate(line_segments)
lc = LineCollection(line_segments.reshape(-1, 2, 2), linewidths=2, colors='blue', alpha=0.5)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.add_collection(lc)
ax.autoscale_view()  # Auto-scale the axis limits based on the line segments

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(-3, 3)
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.colorbar(lc, ax=ax, label='Density of Lines')
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data for distinct solutions (lines)
n_lines = 100
x = np.linspace(0, 10, 100)

# Example solutions with random slopes
slopes = np.random.uniform(-1, 1, n_lines)
intercepts = np.random.uniform(0, 10, n_lines)

# Create line segments with opacity based on some probability
colors = np.random.rand(n_lines, 3)  # Random colors for lines
alphas = np.random.rand(n_lines)  # Random opacity values

# Create list of line segments
lines = []
for slope, intercept in zip(slopes, intercepts):
    y = slope * x + intercept
    lines.append(np.column_stack((x, y)))

# Create a LineCollection from the line segments
lc = LineCollection(lines, colors=colors, linewidths=2, alpha=alphas)

# Create the plot
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.colorbar(lc, ax=ax, label='Line Density')
plt.show()

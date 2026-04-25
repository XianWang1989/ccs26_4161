
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data generation
num_lines = 10
x = np.linspace(0, 10, 100)
solutions = [np.sin(x + i) + (i * 0.5) for i in range(num_lines)]
probabilities = np.random.rand(num_lines)  # Random probabilities for demonstration

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a LineCollection for better blending
lines = []
for i, solution in enumerate(solutions):
    line = np.array([x, solution]).T.reshape(-1, 1, 2)
    color = (1, 0, 0, probabilities[i])  # RGBA (with opacity)
    lines.append(LineCollection(line, colors=color, linewidths=2))

# Add the lines to the axes
for lc in lines:
    ax.add_collection(lc)

# Set the limits and labels
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-3, 3)
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.grid()
plt.show()

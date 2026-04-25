
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize

# Sample data: distinct lines in parameter space
num_lines = 100
x = np.linspace(0, 10, 100)
lines = []

# Generate lines with varying probabilities
for i in range(num_lines):
    y = np.sin(x + (i * 2 * np.pi / num_lines)) + np.random.normal(0, 0.1, x.shape)
    prob = np.random.rand()  # Random probability for opacity
    lines.append((x, y, prob))

# Create figure and axis
fig, ax = plt.subplots()

# Normalize the probabilities for coloring
norm = Normalize(vmin=0, vmax=1)

# Plotting each line with varying opacity
for xs, ys, prob in lines:
    ax.add_line(plt.Line2D(xs, ys, lw=2, alpha=prob, color=plt.cm.viridis(norm(prob))))

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')
ax.set_title('Density Plot with Distinct Lines')

# Show the plot
plt.show()

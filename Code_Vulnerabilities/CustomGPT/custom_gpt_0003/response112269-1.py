
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data for distinct solutions
np.random.seed(0)
num_lines = 10
x = np.linspace(0, 10, 100)
lines = []
probabilities = []

for i in range(num_lines):
    # Create a distinct line with some variation
    y = np.sin(x + i) + (np.random.rand(*x.shape) * 0.5)  # Adding noise
    lines.append(np.array([x, y]).T)
    probabilities.append(np.random.rand())  # Random probabilities for each line

# Create a LineCollection with varying colors based on probabilities
colors = plt.cm.viridis(probabilities)

# Create line segments for each line
line_segments = [np.array(lines[i]) for i in range(num_lines)]
lc = LineCollection(line_segments, linewidths=2, colors=colors, alpha=0.6)

# Create the plot
fig, ax = plt.subplots()
ax.add_collection(lc)

# Set limits
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')

# Show the plot
plt.colorbar(lc, ax=ax, label='Probability')
plt.show()

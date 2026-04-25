
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data
n_lines = 50
x = np.linspace(-5, 5, 100)
lines = [x, np.sin(x + np.random.uniform(0, 2 * np.pi)) * (i/n_lines) for i in range(n_lines)]

# Create a LineCollection
line_segments = np.array([[[x[i], line[i]], [x[i+1], line[i+1]]] for line in lines for i in range(len(x) - 1)])
probabilities = np.linspace(0, 1, n_lines)  # Example probabilities

# Set opacity based on probability
colors = plt.cm.viridis(probabilities)

# Create the plot
fig, ax = plt.subplots()
line_collection = LineCollection(line_segments, colors=colors, linewidths=2, alpha=0.6)
ax.add_collection(line_collection)

# Set limits and labels
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 1)
ax.set_title('Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.colorbar(line_collection, ax=ax, label='Probability')
plt.show()

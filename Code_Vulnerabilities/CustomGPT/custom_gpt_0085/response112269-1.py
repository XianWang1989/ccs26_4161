
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct lines in parameter space
x = np.linspace(0, 10, 100)
solutions = [
    (x, np.sin(x) + np.random.normal(0, 0.1, size=x.shape), 0.5),
    (x, np.cos(x) + np.random.normal(0, 0.1, size=x.shape), 0.3),
    (x, np.sin(x + 1) + np.random.normal(0, 0.1, size=x.shape), 0.8)
]

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

# Create a LineCollection for each distinct solution
for sol in solutions:
    x_data, y_data, probability = sol
    points = np.array([x_data, y_data]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, linewidths=2, alpha=probability, color='b')
    ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('2D Density Plot with Distinct Lines')

# Show grid
ax.grid()

# Show the plot
plt.show()

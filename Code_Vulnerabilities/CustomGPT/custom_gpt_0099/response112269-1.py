
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data: distinct lines in parameter space
np.random.seed(0)
num_lines = 100
x = np.linspace(0, 10, 100)
lines = []

# Create distinct linear solutions with varying probabilities
for i in range(num_lines):
    y = np.sin(x + (i * np.pi) / 10) + np.random.normal(scale=0.1, size=x.shape)
    probability = np.random.rand()  # Random probability for each line
    lines.append((x, y, probability))

# Create a LineCollection object
segments = []
colors = []
for x, y, prob in lines:
    segments.append(np.array([x, y]).T)  # Create segments
    colors.append((0, 0, 0, prob))  # RGBA color with varying alpha

# Create a LineCollection
line_collection = LineCollection(segments, colors=colors, linewidths=2)

# Create a plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.add_collection(line_collection)
ax.autoscale_view()
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')
plt.grid(True)
plt.show()

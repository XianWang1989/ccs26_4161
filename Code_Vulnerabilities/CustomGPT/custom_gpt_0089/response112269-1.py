
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data
num_lines = 50
x = np.linspace(0, 10, 100)
lines = []

# Create distinct lines with varying probabilities
for i in range(num_lines):
    y = np.sin(x + i * np.pi / 10) + np.random.normal(scale=0.1, size=x.shape)
    lines.append((x, y, np.random.rand()))  # (x, y, opacity)

# Create a LineCollection
segments = []
colors = []

for line in lines:
    x_data, y_data, opacity = line
    segments.append(np.column_stack([x_data, y_data]))
    colors.append((0, 0, 0, opacity))  # Black with varying opacity

# Create the collection
line_collection = LineCollection(segments, colors=colors, linewidths=2)

# Plotting
fig, ax = plt.subplots()
ax.add_collection(line_collection)
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-2, 2)
ax.set_title("2D Density Plot with Distinct Lines")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
plt.colorbar(line_collection, ax=ax, label="Opacity")

plt.show()

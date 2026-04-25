
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate some sample data
np.random.seed(0)
n_lines = 10
x = np.linspace(0, 10, 100)

# Create some distinct solutions (lines)
y_lines = []
for i in range(n_lines):
    y = np.sin(x + i) + np.random.normal(scale=0.1, size=x.shape)
    y_lines.append(y)

# Create a line collection with varying alpha based on some probability
line_segments = []
norm = plt.Normalize(0, n_lines)  # Normalize based on the number of lines
for i, y in enumerate(y_lines):
    segments = np.array([x, y]).T.reshape(-1, 1, 2)
    line_segments.append(LineCollection(segments, colors='blue', alpha=norm(i) / n_lines, linewidth=2))

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
for line in line_segments:
    ax.add_collection(line)

ax.set_xlim(x.min(), x.max())
ax.set_ylim(-2, 2)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Density Plot of Distinct Lines')
plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap='Blues'), ax=ax, label='Probability')
plt.grid()
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: creating distinct solutions
np.random.seed(0)
num_lines = 10
x = np.linspace(0, 10, 100)
lines = []

for i in range(num_lines):
    y = np.sin(x + i) + np.random.normal(0, 0.1, size=x.shape)
    lines.append((x, y))

# Create LineCollection for additive blending
line_segments = []
probabilities = []

for i, (x, y) in enumerate(lines):
    segments = np.array([x, y]).T.reshape(-1, 1, 2)
    line_segments.append(segments)
    probabilities.append(0.1 + i * 0.09)  # Example probabilities

# Combine all segments
all_segments = np.vstack(line_segments)
all_probabilities = np.repeat(probabilities, 100).reshape(-1, 1)

# Create LineCollection
lc = LineCollection(all_segments, linewidths=2, alpha=1, cmap='viridis')
lc.set_array(all_probabilities)
lc.set_norm(plt.Normalize(0, 1))

# Plot
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
plt.colorbar(lc, ax=ax, label='Probability')
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

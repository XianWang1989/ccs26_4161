import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Example: create a set of lines (distinct solutions)
num_lines = 100
x = np.linspace(0, 10, 100)
lines = []

for i in range(num_lines):
    y = np.sin(x + np.random.uniform(0, 2*np.pi)) + 0.1 * np.random.randn(len(x))
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lines.append(segments)

# Flatten list of line segments
all_segments = np.vstack(lines)

# Use a LineCollection for efficient rendering
lc = LineCollection(all_segments, linewidths=0.5, alpha=0.03, color='black')

fig, ax = plt.subplots(figsize=(8, 6))
ax.add_collection(lc)
ax.autoscale()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-2, 2)
ax.set_xlabel("Parameter 1")
ax.set_ylabel("Parameter 2")
ax.set_title("Density Plot of Distinct Line Solutions")

plt.show()

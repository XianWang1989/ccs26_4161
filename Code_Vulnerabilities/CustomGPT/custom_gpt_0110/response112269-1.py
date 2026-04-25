
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Example data: distinct lines in parameter space
# Each line is represented by its endpoints
lines = [
    np.array([[0, 0], [1, 1]]),
    np.array([[0, 1], [1, 0]]),
    np.array([[0, 0], [0.5, 1]]),
    np.array([[0.5, 0], [1, 1]]),
]

# Create a figure
plt.figure(figsize=(8, 8))

# Create a colormap
cmap = plt.cm.viridis

# Draw each line with varying opacity
for idx, line in enumerate(lines):
    # Generate line segments for better opacity control
    points = np.array(line)
    segments = np.array([points[:-1], points[1:]]).transpose((1, 0, 2))
    lc = LineCollection(segments, linewidths=2, colors=[cmap(idx / len(lines))], alpha=0.5)
    plt.gca().add_collection(lc)

# Set limits and labels
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.title('2D Density Plot with Distinct Lines')
plt.grid(True)

# Show the plot
plt.show()

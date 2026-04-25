
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Create sample data
# Let's say we have 5 distinct lines
x = np.linspace(0, 10, 100)
lines = [
    (x, np.sin(x) + i) for i in range(5)
]  # 5 sine waves

# Assign probabilities (opacity) to each line
probabilities = np.array([0.5, 0.7, 0.9, 0.4, 0.6])

# Create a LineCollection with varying alpha based on probabilities
segments = np.array(lines)
line_segments = np.array([segments[i] for i in range(len(segments))])

# Create a collection of line segments
lc = LineCollection(line_segments, linewidths=2, colors='blue',
                    alpha=1 / probabilities)

# Create plot
plt.figure(figsize=(10, 6))
ax = plt.gca()
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)
plt.title("Density Plot with Distinct Lines")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()

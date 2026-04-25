
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data
num_lines = 50
x = np.linspace(0, 10, 100)
lines = []

# Create distinct lines with varying probabilities
for i in range(num_lines):
    y = np.sin(x + np.random.rand() * 2 * np.pi) + i * 0.1
    probability = np.random.rand() # Random probability for opacity
    lines.append((x, y, probability))

# Prepare line segments for LineCollection
segments = []
norm = plt.Normalize(0, 1)  # Normalize probabilities for color mapping

for x, y, prob in lines:
    segments.append((x, y, prob))

# Create LineCollection
line_segments = [([x[i], x[i+1]], [y[i], y[i+1]], prob) for x, y, prob in segments for i in range(len(x)-1)]
lc = LineCollection(line_segments, colors='blue', linewidths=2,
                    alpha=[norm(prob) for _, _, prob in line_segments])

# Create plot
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.set_xlim(0, 10)
ax.set_ylim(-1, num_lines * 0.1)
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
plt.colorbar(lc, ax=ax, label='Probability')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data: distinct lines with probabilities
num_lines = 5
x_values = np.linspace(0, 10, 100)

# Example lines and their associated probabilities
lines = []
probabilities = np.random.rand(num_lines)  # Random probabilities for each line

for prob in probabilities:
    slope = np.random.uniform(-1, 1)  # Random slope
    intercept = np.random.uniform(0, 5)  # Random intercept
    y_values = slope * x_values + intercept
    lines.append((x_values, y_values, prob))

# Create a LineCollection
segments = []
colors = []
for x, y, prob in lines:
    segments.append(np.array([x, y]).T)
    colors.append((0, 0, 0, prob))  # Black color with alpha as probability

# Convert to a numpy array for LineCollection
segments = np.concatenate(segments)
colors = np.array(colors)

lc = LineCollection(segments, colors=colors, linewidths=2)
fig, ax = plt.subplots()
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('2D Density Plot with Distinct Lines')

plt.colorbar(lc, label='Opacity/Probability')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Dummy data: create a list of lines
data = [
    (np.arange(0, 10), np.random.rand(10) + 1),  # Line 1
    (np.arange(0, 10), np.random.rand(10) + 3),  # Line 2
    (np.arange(0, 10), np.random.rand(10) + 5),  # Line 3
]

# Probability values for opacity
probabilities = [0.8, 0.5, 0.3]  # Change as needed

# Create a figure and axis
fig, ax = plt.subplots()

# Create a LineCollection
segments = []
colors = []

for (x, y), prob in zip(data, probabilities):
    segments.append(np.array([x, y]).T)
    colors.append((0, 0, 0, prob))  # RGBA: RGB = 0, 0, 0 (black) and alpha = prob

# Create the collection
lc = LineCollection(segments, linewidths=2, colors=colors)
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Density Plot with Distinct Lines')

plt.show()

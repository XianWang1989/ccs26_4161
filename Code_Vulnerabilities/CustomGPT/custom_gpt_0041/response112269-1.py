
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

# Sample data: distinct solutions represented as line segments
x_data = [np.linspace(1, 10, 100), np.linspace(1, 10, 100) + 2]
y_data = [np.sin(x) + i for i, x in enumerate(x_data)]

# Probability corresponding to each line (for opacity)
probabilities = [0.5, 0.8]

# Create a LineCollection
lines = []
for x, y, prob in zip(x_data, y_data, probabilities):
    line = np.array([x, y]).T.reshape(-1, 1, 2)  # Reshape for LineCollection
    lines.append((line, prob))

# Plotting
fig, ax = plt.subplots()

for line, prob in lines:
    collection = LineCollection(line, linewidths=2, colors='b', alpha=prob)
    ax.add_collection(collection)

# Set axis limits
ax.set_xlim(0, 11)
ax.set_ylim(-2, 2)

# Add colorbar to represent probabilities (optional)
cbar = plt.colorbar(collection, ax=ax, orientation='vertical')
cbar.set_label('Probability')

# Show plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

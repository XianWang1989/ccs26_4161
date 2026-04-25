
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct lines (x, y) and corresponding probabilities
lines = [
    (np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)) + i) for i in range(5)
]
probabilities = [0.1, 0.3, 0.5, 0.7, 0.9]  # Corresponding probabilities

# Creating a figure and axis
fig, ax = plt.subplots()

# Plot each line with a corresponding opacity (alpha)
for i, (x, y) in enumerate(lines):
    ax.plot(x, y, alpha=probabilities[i], linewidth=2)

# Adjusting the limits for better visibility
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)

# Adding labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Density Plot with Distinct Lines')

# Show the plot
plt.show()

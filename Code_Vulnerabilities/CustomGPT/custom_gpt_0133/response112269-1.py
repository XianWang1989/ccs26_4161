
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Example data - distinct lines in parameter space
lines = [
    (np.linspace(0, 1, 100), np.linspace(0, 1, 100) + np.random.normal(0, 0.1, 100)), # Line 1
    (np.linspace(0, 1, 100), np.linspace(0, 1, 100) + 0.5 + np.random.normal(0, 0.1, 100)), # Line 2
    (np.linspace(0, 1, 100), np.linspace(0, 1, 100) + 1.0 + np.random.normal(0, 0.1, 100)), # Line 3
]

# Create a figure and axes
fig, ax = plt.subplots()

# Create a LineCollection for better blending
for line in lines:
    x = line[0]
    y = line[1]
    # Probability for opacity
    prob = np.random.rand()  # Random probability for demonstration
    alpha = prob  # Set line opacity based on probability
    ax.plot(x, y, alpha=alpha, linewidth=2)

# Set limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 2)
ax.set_title('Density Plot with Distinct Lines')
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')

# Show the plot
plt.show()

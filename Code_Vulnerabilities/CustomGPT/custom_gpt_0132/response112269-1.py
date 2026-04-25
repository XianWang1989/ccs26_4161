
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct lines in the parameter space
lines = [
    np.array([[0, 0], [1, 1]]),
    np.array([[0, 1], [1, 0]]),
    np.array([[0, 0], [1, 0.5]])
]

# Create a matplotlib figure and axis
fig, ax = plt.subplots()

# Create LineCollection
for line in lines:
    # Probability corresponding to the line for opacity
    probability = np.random.rand()  # Replace with actual probability
    lc = LineCollection([line],
                        colors='blue',
                        linewidths=2,
                        alpha=probability)  # Set opacity based on probability
    ax.add_collection(lc)

# Set limits and aspect
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')

# Add grid and labels
ax.grid(True)
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.set_title('2D Density Plot with Distinct Lines')

# Show plot
plt.show()

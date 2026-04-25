
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct lines represented as arrays of x and y coordinates
lines = [
    (np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.1, 100), 0.8),
    (np.linspace(0, 10, 100), np.cos(np.linspace(0, 10, 100)) + np.random.normal(0, 0.1, 100), 0.6),
    (np.linspace(0, 10, 100), np.linspace(0, 5, 100) + np.random.normal(0, 0.1, 100), 0.4),
]

# Create figure and axis
fig, ax = plt.subplots()

# Plot each line with varying opacity based on its probability
for x, y, alpha in lines:
    ax.plot(x, y, alpha=alpha, linewidth=2)

# Enhance the plot's aesthetics
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.grid(True)

# Show the plot
plt.show()

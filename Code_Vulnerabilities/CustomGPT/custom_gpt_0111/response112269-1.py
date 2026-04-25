
import numpy as np
import matplotlib.pyplot as plt

# Sample data: lines defined by arrays of x and y coordinates
solutions = [
    (np.linspace(-2, 2, 100), np.linspace(-1, 1, 100)**2), # First line
    (np.linspace(-2, 2, 100), np.sin(np.linspace(-2, 2, 100))), # Second line
    (np.linspace(-2, 2, 100), 0.2 * np.linspace(-2, 2, 100)), # Third line
]

# Probabilities corresponding to each line for opacity
probabilities = [0.5, 0.8, 1.0]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each solution with varying opacity
for (x, y), prob in zip(solutions, probabilities):
    ax.plot(x, y, alpha=prob, lw=2)  # Adjust the linewidth (lw) as needed

# Set the axis limits and labels
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-3, 3)
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')

# Add a grid for better visibility
ax.grid(True)

# Show the plot
plt.title('Density Plot of Distinct Solutions')
plt.show()

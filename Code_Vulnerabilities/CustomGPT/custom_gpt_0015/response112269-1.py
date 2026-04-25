
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data for distinct lines
x = np.linspace(0, 10, 100)
line1 = np.sin(x) + 1
line2 = np.cos(x) + 1.5
line3 = np.sin(x + np.pi / 4) + 2

# Define line probabilities (opacity)
probabilities = [0.5, 0.7, 0.9]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each line with corresponding opacity
for i, line in enumerate([line1, line2, line3]):
    ax.plot(x, line, alpha=probabilities[i], linewidth=3)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(0, 3.5)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('2D Density Plot with Distinct Lines')

# Show the plot
plt.show()

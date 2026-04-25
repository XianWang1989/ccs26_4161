
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct solutions as lines
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + 2  # First line

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) + 1  # Second line

# Number of lines and their opacities
solutions = [(x1, y1, 0.5), (x2, y2, 0.5)]
colors = ['blue', 'orange']

# Create a figure
plt.figure(figsize=(10, 6))

# Plot each line
for (x, y, alpha), color in zip(solutions, colors):
    plt.plot(x, y, color=color, alpha=alpha)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Parameter Space Density Plot with Distinct Lines')

# Show grid
plt.grid()

# Show the plot
plt.show()

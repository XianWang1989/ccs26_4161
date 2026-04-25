
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
num_lines = 10
x_values = np.linspace(-5, 5, 100)
solutions = [np.sin(x_values + i) + (i * 0.5) for i in range(num_lines)]

# Create a figure
plt.figure(figsize=(10, 6))

# Plot each solution line with varying opacity
for i, solution in enumerate(solutions):
    plt.plot(x_values, solution, alpha=0.1 + 0.1 * i, linewidth=2)

# Enhance boundaries
plt.xlim(-5, 5)
plt.ylim(-7, 7)
plt.title("2D Density Plot with Distinct Lines")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the grid
plt.grid()

# Show the plot
plt.show()

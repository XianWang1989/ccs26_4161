
import numpy as np
import matplotlib.pyplot as plt

# Example data: Intersection of distinct lines
x = np.linspace(0, 10, 100)
solutions = [
    (x, 0.1 * np.sin(x) + 5, 0.3),  # Line 1
    (x, 0.2 * np.cos(x) + 5, 0.5),  # Line 2
    (x, 0.3 * np.sin(x + 1) + 4.5, 0.7),  # Line 3
]

# Create the plot
plt.figure(figsize=(10, 8))

# Plot each solution line
for solution in solutions:
    x_data, y_data, alpha = solution
    plt.plot(x_data, y_data, alpha=alpha, linewidth=2)

# Set aesthetics
plt.title('2D Density Plot of Distinct Solutions')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(0, 10)

# Show the plot
plt.show()

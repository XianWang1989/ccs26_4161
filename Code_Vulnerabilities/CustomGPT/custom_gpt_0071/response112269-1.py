
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct solutions (lines)
num_lines = 100
x = np.linspace(-5, 5, 100)
solutions = []

# Generate distinct solutions with varying probabilities
for i in range(num_lines):
    y = np.sin(x + i * 0.1) + np.random.normal(0, 0.1, x.shape)
    solutions.append((x, y))

# Probability representation (for opacity)
probabilities = np.linspace(0.1, 1, num_lines)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each solution as a line
for (x_line, y_line), prob in zip(solutions, probabilities):
    plt.plot(x_line, y_line, alpha=prob, linewidth=1)

plt.title('2D Density Plot of Distinct Solutions')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid()
plt.show()

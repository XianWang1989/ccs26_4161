
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data: distinct line solutions
num_lines = 50
x = np.linspace(-10, 10, 100)
solutions = [x, 0.1 * x + i for i in np.linspace(-5, 5, num_lines)]

# Simulate probabilities for each line
probabilities = np.random.rand(num_lines)

# Create the figure and axis
plt.figure(figsize=(10, 6))

# Plot each solution with varying opacity based on probabilities
for i, sol in enumerate(solutions):
    y = sol
    plt.plot(x, y, color='blue', alpha=probabilities[i], lw=2)

# Set the limits and labels
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)

# Show the plot
plt.show()

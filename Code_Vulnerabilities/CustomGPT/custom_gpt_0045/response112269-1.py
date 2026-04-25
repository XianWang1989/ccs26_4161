
import numpy as np
import matplotlib.pyplot as plt

# Example data: distinct solutions
x = np.linspace(0, 10, 100)

# Define multiple solutions with varying opacity
solutions = [
    np.sin(x) + i for i in range(3)  # Different sine waves for illustrative purposes
]

# Probability values associated with each solution
probabilities = [0.2, 0.5, 0.8]  # Adjust these values to vary opacity

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot each solution line with varying opacity
for i, solution in enumerate(solutions):
    plt.plot(x, solution, lw=2, alpha=probabilities[i], label=f'Solution {i+1}')

# Optionally adding fill between lines to emphasize the density (with lower opacity)
for i, solution in enumerate(solutions):
    plt.fill_between(x, solution, alpha=0.1 * probabilities[i], color=f'C{i}', label=f'Area {i+1}')

plt.title('Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.legend()
plt.grid(True)
plt.xlim([0, 10])
plt.ylim([-3, 3])

# Show the plot
plt.show()

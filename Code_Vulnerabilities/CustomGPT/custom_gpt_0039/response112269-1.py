
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct lines in 2D space
num_lines = 10
x = np.linspace(-5, 5, 100)

# Generating distinct solutions (lines)
solutions = [np.sin(x + i) + i*0.1 for i in range(num_lines)]
probabilities = np.linspace(0.1, 1, num_lines)  # Example probabilities

# Create figure
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity based on probability
for i, solution in enumerate(solutions):
    plt.plot(x, solution, alpha=probabilities[i], linewidth=2, label=f'Solution {i+1}')

plt.title('Density Plot of Distinct Solutions')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', lw=0.5, ls='--')  # Horizontal line at y=0
plt.axvline(0, color='black', lw=0.5, ls='--')  # Vertical line at x=0
plt.legend()
plt.grid()
plt.show()

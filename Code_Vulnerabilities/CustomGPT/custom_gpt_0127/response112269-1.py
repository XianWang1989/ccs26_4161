
import numpy as np
import matplotlib.pyplot as plt

# Sample data: Create distinct lines in 2D parameter space
x = np.linspace(0, 10, 100)
solutions = [np.sin(x + np.random.rand() * 2 * np.pi) + i for i in range(5)]

# Corresponding probabilities for each solution (0 to 1)
probabilities = np.random.rand(len(solutions))

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each solution line with varying opacity
for i, solution in enumerate(solutions):
    ax.plot(x, solution + i, alpha=probabilities[i], linewidth=2, label=f'Solution {i + 1}')

# Customize plot
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.legend()
ax.set_ylim(-1, len(solutions))

# Show the plot
plt.show()

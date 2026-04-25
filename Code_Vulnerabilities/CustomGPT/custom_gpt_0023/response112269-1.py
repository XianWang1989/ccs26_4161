
import numpy as np
import matplotlib.pyplot as plt

# Sample data
n_lines = 100
x = np.linspace(0, 10, 100)
solutions = [np.sin(x + np.random.rand()) + i for i in range(n_lines)]

# Probability values for each line (can be customized)
probabilities = np.random.rand(n_lines)

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot each solution as a line with varying opacity based on probability
for solution, prob in zip(solutions, probabilities):
    plt.plot(x, solution, alpha=prob, color='blue')

# Customize axis labels and title
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.title('2D Density Plot with Distinct Lines')
plt.grid()

# Show the plot
plt.show()

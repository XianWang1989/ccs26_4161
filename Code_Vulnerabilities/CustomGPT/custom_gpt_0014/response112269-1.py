
import numpy as np
import matplotlib.pyplot as plt

# Example parameters
num_points = 1000
num_solutions = 5
x = np.linspace(-5, 5, num_points)
y_values = [np.sin(x + np.random.uniform(0, 2*np.pi)) + i for i in range(num_solutions)]
probabilities = np.random.rand(num_solutions)

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot each solution as a line with opacity based on its probability
for i in range(num_solutions):
    plt.plot(x, y_values[i], alpha=probabilities[i], label=f'Solution {i+1}', linewidth=2)

# Customize the plot
plt.title('2D Density Plot of Distinct Solutions')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)
plt.legend()
plt.xlim(-5.5, 5.5)
plt.ylim(-3, 3)

# Show the plot
plt.show()

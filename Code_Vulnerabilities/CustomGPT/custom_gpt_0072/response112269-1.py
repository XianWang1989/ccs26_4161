
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
num_lines = 10
x = np.linspace(0, 10, 100)

# Create distinct line solutions with random slopes and intercepts
solutions = [0.1 * i * x + np.random.normal(0, 0.5, x.shape) for i in range(1, num_lines + 1)]
probabilities = np.linspace(0.1, 1, num_lines)  # Example probabilities

# Create the plot
plt.figure(figsize=(8, 8))

# Plot each solution
for solution, prob in zip(solutions, probabilities):
    plt.plot(x, solution, alpha=prob, linewidth=2)

# Customize the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter 1')
plt.ylabel('Parameter 2')
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(-5, 10)

# Show the plot
plt.show()

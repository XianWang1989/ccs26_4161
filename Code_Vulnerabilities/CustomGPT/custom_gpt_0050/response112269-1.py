
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
n_lines = 200
x = np.linspace(-3, 3, 100)
solutions = [x + np.random.normal(scale=0.1, size=x.shape) for _ in range(n_lines)]
probabilities = np.random.rand(n_lines)  # Random probabilities

# Setting up the plot
plt.figure(figsize=(8, 6))

# Plot each solution line with varying opacity
for solution, prob in zip(solutions, probabilities):
    plt.plot(x, solution, color='blue', alpha=prob/2)  # Scale opacity by probability

# Customizing the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

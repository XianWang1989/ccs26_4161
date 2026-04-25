
import numpy as np
import matplotlib.pyplot as plt

# Example data: distinct solutions represented as lines
x = np.linspace(0, 10, 100)
solutions = [np.sin(x + phase) + (i * 0.2) for i, phase in enumerate([0, np.pi/4, np.pi/2])]

plt.figure(figsize=(8, 6))

# Plot each solution with varying opacity based on some probability
probabilities = [0.5, 0.3, 0.7]  # Example probabilities for alpha blending
colors = ['red', 'green', 'blue']

for solution, alpha, color in zip(solutions, probabilities, colors):
    plt.plot(x, solution, color=color, alpha=alpha)

# Set axes, labels, and title
plt.xlim(0, 10)
plt.ylim(-2, 2)
plt.xlabel('Parameter 1')
plt.ylabel('Parameter 2')
plt.title('2D Density Plot with Distinct Lines')

plt.grid()
plt.show()

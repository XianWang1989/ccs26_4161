
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data (change as needed)
num_lines = 10
x = np.linspace(0, 1, 100)

# Random slopes and intercepts for demonstration
slopes = np.random.uniform(-1, 1, num_lines)
intercepts = np.random.uniform(0, 1, num_lines)
probabilities = np.random.uniform(0, 1, num_lines)  # Probabilities for opacity

plt.figure(figsize=(10, 6))

# Plot each line with opacity based on probability
for slope, intercept, prob in zip(slopes, intercepts, probabilities):
    y = slope * x + intercept
    plt.plot(x, y, alpha=prob, linewidth=2)

plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True)
plt.show()

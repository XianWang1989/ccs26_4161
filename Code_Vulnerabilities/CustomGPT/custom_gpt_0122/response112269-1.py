
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
x = np.linspace(-5, 5, 100)
y1 = 0.5 * x + np.random.normal(scale=0.5, size=x.shape)  # First line
y2 = -0.5 * x + np.random.normal(scale=0.5, size=x.shape)  # Second line
y3 = np.sin(x) + np.random.normal(scale=0.5, size=x.shape)  # Third line

# Define probabilities (alpha values) for each line
probabilities = [0.3, 0.6, 0.9]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity
plt.plot(x, y1, alpha=probabilities[0], color='blue', label='Solution 1')
plt.plot(x, y2, alpha=probabilities[1], color='orange', label='Solution 2')
plt.plot(x, y3, alpha=probabilities[2], color='green', label='Solution 3')

# Customize the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.axhline(0, color='gray', lw=0.5, ls='--')
plt.axvline(0, color='gray', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()

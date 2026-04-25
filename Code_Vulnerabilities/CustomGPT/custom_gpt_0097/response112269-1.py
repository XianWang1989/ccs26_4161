
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data: distinct solutions as lines
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, x.size)
y2 = np.cos(x) + np.random.normal(0, 0.1, x.size)
y3 = 0.5 * np.sin(x + 1) + np.random.normal(0, 0.1, x.size)

# Define probabilities for opacity
probabilities = [0.7, 0.5, 0.9]

# Plot each line with varying opacity
plt.figure(figsize=(8, 6))
for y, prob in zip([y1, y2, y3], probabilities):
    plt.plot(x, y, alpha=prob, linewidth=2)

# Customize the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(-2, 2)
plt.show()

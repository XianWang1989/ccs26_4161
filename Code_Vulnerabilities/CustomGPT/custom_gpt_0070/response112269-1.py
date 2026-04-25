
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct solutions in parameter space
x = np.linspace(-5, 5, 100)
y1 = 0.1 * x**2
y2 = -0.1 * (x**2) + 5
y3 = np.sin(x) + 2
y4 = np.cos(x) + 2

# Probability weights for each solution
weights = [0.3, 0.6, 0.5, 0.4]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity based on its weight
plt.plot(x, y1, color='blue', alpha=weights[0], linewidth=2, label='Solution 1')
plt.plot(x, y2, color='green', alpha=weights[1], linewidth=2, label='Solution 2')
plt.plot(x, y3, color='red', alpha=weights[2], linewidth=2, label='Solution 3')
plt.plot(x, y4, color='purple', alpha=weights[3], linewidth=2, label='Solution 4')

# Customize the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid()
plt.legend()

# Show the plot
plt.show()

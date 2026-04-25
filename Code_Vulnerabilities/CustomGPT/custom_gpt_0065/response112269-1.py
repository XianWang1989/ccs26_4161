
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct solutions forming lines in parameter space
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, x.shape)
y2 = np.cos(x) + np.random.normal(0, 0.1, x.shape)
y3 = 0.5 * np.sin(2 * x) + np.random.normal(0, 0.1, x.shape)

# Define the alpha levels for transparency
alpha_levels = [0.3, 0.5, 0.7]

# Create a figure
plt.figure(figsize=(8, 6))

# Plot each line with different alpha levels
plt.plot(x, y1, color='red', alpha=alpha_levels[0], label='Solution 1')
plt.plot(x, y2, color='blue', alpha=alpha_levels[1], label='Solution 2')
plt.plot(x, y3, color='green', alpha=alpha_levels[2], label='Solution 3')

# Set labels and title
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.title('2D Density Plot with Distinct Lines')
plt.legend()
plt.grid()

# Show the plot
plt.show()

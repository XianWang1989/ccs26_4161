
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct solutions in parameter space
x1 = np.linspace(0, 10, 100)
y1 = 2 * np.sin(x1) + 2
p1 = np.exp(-((x1 - 5)**2 + (y1 - 5)**2)/8)  # Probability distribution for line 1

x2 = np.linspace(0, 10, 100)
y2 = 1.5 * np.cos(x2) + 5
p2 = np.exp(-((x2 - 7)**2 + (y2 - 5)**2)/8)  # Probability distribution for line 2

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each line with color and opacity based on their probability
plt.plot(x1, y1, color='blue', alpha=0.5 * p1 / p1.max(), label='Solution 1')
plt.plot(x2, y2, color='red', alpha=0.5 * p2 / p2.max(), label='Solution 2')

# Add a color legend
plt.colorbar(plt.cm.ScalarMappable(cmap='Blues'), label='Density Probability')

# Customize the plot appearance
plt.title('Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)
plt.legend()
plt.xlim(0, 10)
plt.ylim(0, 10)

# Show the plot
plt.show()

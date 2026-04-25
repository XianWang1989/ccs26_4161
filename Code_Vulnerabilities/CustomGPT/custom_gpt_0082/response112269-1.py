
import numpy as np
import matplotlib.pyplot as plt

# Generate example data
# Assume we have 3 distinct solutions represented by lines
x = np.linspace(0, 10, 100)
y1 = 0.2 * x + np.random.normal(0, 0.5, x.shape)
y2 = 0.5 * x + np.random.normal(0, 0.5, x.shape)
y3 = -0.3 * x + np.random.normal(0, 0.5, x.shape)

# Define probabilities for the lines (0-1 scale)
probabilities = [0.8, 0.5, 0.3]

# Create a density plot
plt.figure(figsize=(10, 6))
plt.title('Density Plot with Distinct Lines')

# Plot each line with opacity based on its probability
for i, y in enumerate([y1, y2, y3]):
    plt.plot(x, y, alpha=probabilities[i], lw=2, label=f'Solution {i+1} (p={probabilities[i]})')

# Customize the plot
plt.xlim(0, 10)
plt.ylim(-5, 10)
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid()
plt.legend()
plt.show()

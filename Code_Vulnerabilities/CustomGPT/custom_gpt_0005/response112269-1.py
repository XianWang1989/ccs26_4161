
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
num_lines = 10
x = np.linspace(-5, 5, 100)
y_values = [np.sin(x + i) + np.random.normal(scale=0.1, size=x.shape) for i in range(num_lines)]
probabilities = np.random.rand(num_lines)  # Random probabilities for each line

# Create a transparency scaling based on probabilities
alpha = probabilities / np.max(probabilities)

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity
for y, a in zip(y_values, alpha):
    plt.plot(x, y, alpha=a)

plt.title('Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)
plt.show()

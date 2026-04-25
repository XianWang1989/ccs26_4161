
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
num_lines = 10
x = np.linspace(-5, 5, 100)
y = [np.sin(x + i) + np.random.normal(0, 0.1, x.shape) for i in range(num_lines)]

# Create the plot
plt.figure(figsize=(10, 6))

for i, line in enumerate(y):
    # Use opacity based on the index or any probability measure
    plt.plot(x, line, alpha=(i + 1) / num_lines, linewidth=2)

plt.title('Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.xlim(-5, 5)
plt.ylim(-2, 2)
plt.show()

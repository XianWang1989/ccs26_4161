
import numpy as np
import matplotlib.pyplot as plt

# Generate example data: distinct lines representing solutions
x_values = np.linspace(0, 10, 100)
lines = [
    (x_values, 0.5 * x_values + np.random.normal(0, 0.5, x_values.size), 0.8),  # line 1
    (x_values, 2 * x_values - 5 + np.random.normal(0, 0.5, x_values.size), 0.6),  # line 2
    (x_values, -0.5 * x_values + 5 + np.random.normal(0, 0.5, x_values.size), 0.4)  # line 3
]

# Create a figure and axis
plt.figure(figsize=(8, 6))

# Plot each line with varying opacity
for (x, y, alpha) in lines:
    plt.plot(x, y, color='blue', alpha=alpha)

plt.title('Density Plot with Distinct Solutions')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(0, 10)
plt.ylim(-5, 10)
plt.grid()
plt.show()

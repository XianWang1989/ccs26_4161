
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct solutions as lines in parameter space
x_lines = np.linspace(-5, 5, 100)
y_lines_1 = np.sin(x_lines) + np.random.normal(0, 0.1, size=x_lines.shape)
y_lines_2 = np.cos(x_lines) + np.random.normal(0, 0.1, size=x_lines.shape)
y_lines_3 = 0.5 * np.sin(2 * x_lines) + np.random.normal(0, 0.1, size=x_lines.shape)

# Create a figure
plt.figure(figsize=(10, 6))

# Plot each line with a corresponding opacity based on the probability density
plt.plot(x_lines, y_lines_1, alpha=0.6, color='blue', label='Solution 1 (Probability: 0.6)')
plt.plot(x_lines, y_lines_2, alpha=0.8, color='green', label='Solution 2 (Probability: 0.8)')
plt.plot(x_lines, y_lines_3, alpha=0.4, color='red', label='Solution 3 (Probability: 0.4)')

# Add titles and labels
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.grid()
plt.show()

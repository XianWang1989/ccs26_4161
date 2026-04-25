
import numpy as np
import matplotlib.pyplot as plt

# Sample data
# Generate random lines in a 2D parameter space
num_lines = 100
x_values = np.random.uniform(0, 10, num_lines)
y_values = np.random.uniform(0, 10, num_lines)
widths = np.random.uniform(0.1, 0.3, num_lines)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Define an alpha value for transparency
alpha_value = 0.1

# Plot each line with a specified opacity
for i in range(num_lines):
    # Generate a line segment
    x_line = np.linspace(x_values[i] - width, x_values[i] + width, 100)
    y_line = np.linspace(y_values[i] - width, y_values[i] + width, 100)

    ax.plot(x_line, y_line, color='blue', alpha=alpha_value)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')
ax.set_title('2D Density Plot with Distinct Lines')

# Show the plot
plt.grid()
plt.show()

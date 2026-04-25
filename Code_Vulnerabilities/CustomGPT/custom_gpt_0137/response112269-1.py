
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data: distinct lines representing different solutions
param_x = np.linspace(-10, 10, 100)
lines = []
for i in range(5):  # Create 5 distinct lines
    # Each line follows a linear equation with some added noise
    slope = np.random.uniform(-1, 1)
    intercept = np.random.uniform(-10, 10)
    line_y = slope * param_x + intercept + np.random.normal(scale=0.1, size=param_x.shape)
    lines.append((param_x, line_y, np.random.uniform(0.1, 1)))  # Store x, y, and opacity

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each line with varying opacity
for line in lines:
    ax.plot(line[0], line[1], alpha=line[2], color='blue')

# Set plot limits
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])

# Add grid and labels
ax.grid(True)
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')
ax.set_title('Density Plot with Distinct Lines')

# Show the plot
plt.show()

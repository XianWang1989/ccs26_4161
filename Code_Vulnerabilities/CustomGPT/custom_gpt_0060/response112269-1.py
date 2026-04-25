
import numpy as np
import matplotlib.pyplot as plt

# Generate example data for multiple distinct lines (solutions)
# Each line is represented as a separate array of (x, y) coordinates
np.random.seed(42)  # For reproducible results
n_lines = 10  # Number of distinct solutions
x = np.linspace(-5, 5, 100)

# Create a list to hold the lines with varying slopes and intercepts
lines = []
for i in range(n_lines):
    slope = np.random.uniform(-1, 1)  # Random slope
    intercept = np.random.uniform(-5, 5)  # Random intercept
    y = slope * x + intercept
    lines.append(y)

# Set up the plot
plt.figure(figsize=(10, 8))

# Plot each line with a semi-transparent color
for line in lines:
    plt.plot(x, line, color='blue', alpha=0.1)  # Adjust alpha for blending

# Set plot limits
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Add labels and title
plt.xlabel('Parameter 1')
plt.ylabel('Parameter 2')
plt.title('2D Density Plot with Distinct Lines')

# Optional: Adding grid for better visibility
plt.grid(True)

# Show the plot
plt.show()

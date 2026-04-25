
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
# Suppose these are the parameters of distinct solutions
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + np.random.normal(0, 0.1, 100) + 3  # Line 1

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) + np.random.normal(0, 0.1, 100) + 5  # Line 2

# Set up the plot
plt.figure(figsize=(10, 6))

# Define probabilities for opacity
opacity1 = 0.7  # Opacity for the first line
opacity2 = 0.5  # Opacity for the second line

# Plot each solution with varying opacity
plt.plot(x1, y1, color='blue', alpha=opacity1, lw=2, label='Solution 1')
plt.plot(x2, y2, color='red', alpha=opacity2, lw=2, label='Solution 2')

# Add annotations and settings
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

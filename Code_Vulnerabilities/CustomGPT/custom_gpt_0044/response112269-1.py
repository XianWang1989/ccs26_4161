
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
num_lines = 10
x_values = np.linspace(-5, 5, 100)
probabilities = np.random.rand(num_lines)  # Random probabilities for opacity

# Create a figure
plt.figure(figsize=(8, 6))

# Plot distinct lines with varying opacity
for i in range(num_lines):
    y_values = np.sin(x_values + i)  # Each line can represent a different solution
    plt.plot(x_values, y_values, alpha=probabilities[i], label=f'Solution {i+1}')

# Customize the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', lw=0.5, ls='--')  # Add x-axis line
plt.axvline(0, color='black', lw=0.5, ls='--')  # Add y-axis line
plt.legend()
plt.grid(True)

# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
num_lines = 10
x = np.linspace(-3, 3, 100)
probabilities = np.random.rand(num_lines)

# Create a new figure
plt.figure(figsize=(8, 6))

# Plot distinct lines with varying opacity
for i in range(num_lines):
    y = np.sin(x + i) + np.random.normal(0, 0.1, size=x.shape)  # Example line
    plt.plot(x, y, alpha=probabilities[i], label=f'Solution {i + 1}')

# Add labels and legend
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()
plt.xlim(-3, 3)
plt.ylim(-3, 3)

# Show the plot
plt.grid()
plt.show()

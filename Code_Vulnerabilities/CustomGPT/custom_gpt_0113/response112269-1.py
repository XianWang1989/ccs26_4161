
import numpy as np
import matplotlib.pyplot as plt

# Generate random lines as distinct solutions
num_lines = 10
x = np.linspace(0, 10, 100)

# Probability for each line, can be adjusted
probabilities = np.random.rand(num_lines) * 0.5

# Set up the plot
plt.figure(figsize=(10, 6))

# Iterate through each solution and plot with varying opacity
for i in range(num_lines):
    y = np.sin(x) + (i * 0.3)  # Example line function
    plt.plot(x, y, alpha=probabilities[i], color='blue', lw=2)

# Adjust plot limits to make sure all lines are visible
plt.xlim(0, 10)
plt.ylim(-5, 5)
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

plt.show()

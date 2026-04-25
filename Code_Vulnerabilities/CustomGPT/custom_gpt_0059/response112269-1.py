
import numpy as np
import matplotlib.pyplot as plt

# Sample parameters for distinct lines
num_lines = 10
x = np.linspace(0, 10, 100)

# Generate lines with varying probabilities
for i in range(num_lines):
    # Create a line with a probability
    y = np.sin(x + i) + (i / 10)  # Distinct line functions
    probability = 0.1 * (num_lines - i)  # Decreasing probability
    plt.plot(x, y, alpha=probability, linewidth=2)

# Customize the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.xlim(0, 10)
plt.ylim(-1.5, 3)

plt.grid()
plt.show()

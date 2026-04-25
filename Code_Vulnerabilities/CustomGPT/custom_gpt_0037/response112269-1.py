
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
num_lines = 10
x = np.linspace(-5, 5, 100)

# Generate distinct solutions (lines) with different probabilities
for i in range(num_lines):
    # Create a line with some random offset
    y = np.sin(x + np.random.uniform(0, 2 * np.pi)) + np.random.uniform(-1, 1)
    # Set probability (opacity) for the line
    probability = np.random.uniform(0.1, 1)
    plt.plot(x, y, alpha=probability, color='blue')

# Set plot limits and labels
plt.xlim(-5, 5)
plt.ylim(-3, 3)
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid()

# Show the plot
plt.show()

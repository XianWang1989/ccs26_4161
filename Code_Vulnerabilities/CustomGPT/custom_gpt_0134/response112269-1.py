
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
num_lines = 10
x = np.linspace(-5, 5, 100)

# Create distinct solutions as lines
for i in range(num_lines):
    # Generate random slope and intercept
    slope = np.random.uniform(-1, 1)
    intercept = np.random.uniform(-5, 5)
    # Calculate y based on the line equation
    y = slope * x + intercept
    # Calculate opacity based on a probability (for illustration purposes, use a random value)
    opacity = np.random.uniform(0.1, 1)  
    plt.plot(x, y, alpha=opacity, linewidth=2)

# Set limits and labels
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Density Plot with Distinct Lines')
plt.grid()
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.5, linestyle='--')

# Show the plot
plt.show()

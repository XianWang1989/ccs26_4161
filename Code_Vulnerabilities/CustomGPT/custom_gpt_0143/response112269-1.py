
import numpy as np
import matplotlib.pyplot as plt

# Create sample data: multiple distinct lines
num_lines = 10
x_values = np.linspace(0, 10, 100)

# Generating distinct solutions as lines
for i in range(num_lines):
    y_values = np.sin(x_values + i) + (i * 0.1)  # Offset each line slightly
    plt.plot(x_values, y_values, alpha=0.1, color='blue')  # Adjust alpha for blending

# Improve the plot appearance
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(0, 10)
plt.ylim(-2, 2)
plt.grid(True)

# Show the plot
plt.show()

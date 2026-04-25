
import numpy as np
import matplotlib.pyplot as plt

# Create sample data: distinct solutions as lines
num_lines = 10
x = np.linspace(0, 10, 100)
y = [np.sin(x + i) + np.random.normal(0, 0.1, x.shape) for i in range(num_lines)]

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot each line with transparency
for i in range(num_lines):
    plt.plot(x, y[i], color='blue', alpha=0.1, linewidth=2)

# Customize the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.xlim(0, 10)
plt.ylim(-3, 3)
plt.grid()

# Show the plot
plt.show()

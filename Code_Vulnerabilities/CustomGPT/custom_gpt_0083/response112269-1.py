
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
num_lines = 100
x = np.linspace(-10, 10, 100)
y_lines = [np.sin(x + i) + np.random.normal(0, 0.1, len(x)) for i in range(num_lines)]

# Create a density plot
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity
for i, y in enumerate(y_lines):
    plt.plot(x, y, color='blue', alpha=0.1)  # Adjust alpha for transparency

# Use a colormap to enhance visibility of overlaps 
plt.fill_between(x, np.min(y_lines, axis=0), np.max(y_lines, axis=0), color='white', alpha=0.5)
plt.xlim(-10, 10)
plt.ylim(-2, 2)
plt.title('Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

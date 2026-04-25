
import numpy as np
import matplotlib.pyplot as plt

# Example data: distinct lines in parameter space
num_lines = 20
x = np.linspace(0, 10, 100)

# Creating probabilities for each line
probabilities = np.linspace(0.1, 1, num_lines)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each line with varying opacities
for i in range(num_lines):
    y = np.sin(x + i) + np.random.normal(0, 0.1, size=x.shape)
    ax.plot(x, y, alpha=probabilities[i], color='blue')

# Set axis labels and title
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')
ax.set_title('2D Density Plot with Distinct Lines')

plt.show()

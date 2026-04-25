
import numpy as np
import matplotlib.pyplot as plt

# Sample distinct solutions (lines in parameter space)
# Replace these with your actual data
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + 1  # Line 1

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) + 1  # Line 2

x3 = np.linspace(0, 10, 100)
y3 = (x3 / 10) + 1.5  # Line 3

# Let's say these are the probabilities for these solutions
probabilities = [0.5, 0.8, 0.3]  # Example probabilities for each line

# Create a figure and axis
plt.figure(figsize=(8, 6))

# Plot each line with its corresponding opacity
for i, (x, y) in enumerate(zip([x1, x2, x3], [y1, y2, y3])):
    plt.plot(x, y, alpha=probabilities[i], lw=2, label=f'Solution {i+1}')

# Customize the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter Space X')
plt.ylabel('Parameter Space Y')
plt.ylim(0, 3)
plt.xlim(0, 10)
plt.grid(True)
plt.legend()
plt.show()

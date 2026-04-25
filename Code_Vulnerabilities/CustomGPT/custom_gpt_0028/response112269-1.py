
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct lines in parametric space
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + 1

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) + 1

x3 = np.linspace(0, 10, 100)
y3 = np.tan(x3 / 10) + 1

# Probabilities associated with each line
probabilities = [0.3, 0.5, 0.2]  # Example probabilities for blending

# Create density plot
plt.figure(figsize=(10, 6))

# Plot each line with corresponding opacity
plt.plot(x1, y1, color='blue', alpha=probabilities[0], label='Solution 1')
plt.plot(x2, y2, color='orange', alpha=probabilities[1], label='Solution 2')
plt.plot(x3, y3, color='green', alpha=probabilities[2], label='Solution 3')

# Adjust the limits and labels
plt.xlim(0, 10)
plt.ylim(-1, 3)
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.title('2D Density Plot with Distinct Lines')
plt.legend()
plt.grid()

# Show the plot
plt.show()

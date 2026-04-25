
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data for distinct lines
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + 1
x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) - 1
x3 = np.linspace(0, 10, 100)
y3 = x3 / 10

# Define probabilities associated with each line
probabilities = [0.5, 0.8, 0.6]  # Example probabilities

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity
plt.plot(x1, y1, alpha=probabilities[0], color='blue', label='Solution 1')
plt.plot(x2, y2, alpha=probabilities[1], color='red', label='Solution 2')
plt.plot(x3, y3, alpha=probabilities[2], color='green', label='Solution 3')

# Set labels and title
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.title('Density Plot with Distinct Lines')
plt.legend()
plt.grid()

# Show the plot
plt.show()

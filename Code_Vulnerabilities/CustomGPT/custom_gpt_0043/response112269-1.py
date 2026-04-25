
import numpy as np
import matplotlib.pyplot as plt

# Sample data: define the parameter space
x = np.linspace(-5, 5, 100)
y1 = np.sin(x) + np.random.normal(scale=0.1, size=x.shape)  # First solution
y2 = np.cos(x) + np.random.normal(scale=0.1, size=x.shape)  # Second solution
y3 = 0.5 * np.sin(2*x) + np.random.normal(scale=0.1, size=x.shape)  # Third solution

# Probabilities (for opacity levels)
prob1 = np.abs(np.sin(x))  # Example probabilities for lines
prob2 = np.abs(np.cos(x))
prob3 = np.abs(0.5 * np.sin(2*x))

# Normalize probabilities to [0, 1]
prob1 /= prob1.max()
prob2 /= prob2.max()
prob3 /= prob3.max()

# Create a figure
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity
plt.plot(x, y1, color='blue', alpha=prob1, label='Solution 1')
plt.plot(x, y2, color='green', alpha=prob2, label='Solution 2')
plt.plot(x, y3, color='red', alpha=prob3, label='Solution 3')

# Enhance visibility with labels and title
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.legend()

# Show the plot
plt.grid()
plt.show()

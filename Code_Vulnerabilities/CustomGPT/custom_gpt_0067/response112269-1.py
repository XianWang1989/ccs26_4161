
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data: distinct lines in 2D parameter space
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + np.random.normal(0, 0.1, size=x1.shape)

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) + np.random.normal(0, 0.1, size=x2.shape)

x3 = np.linspace(0, 10, 100)
y3 = np.sin(x3 + 1) + np.random.normal(0, 0.1, size=x3.shape)

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot each line with distinct opacity based on an example probability
ax.plot(x1, y1, color='blue', alpha=0.5)
ax.plot(x2, y2, color='green', alpha=0.5)
ax.plot(x3, y3, color='red', alpha=0.5)

# Set labels and title
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')
ax.set_title('2D Density Plot with Distinct Lines')

# Show the plot
plt.show()

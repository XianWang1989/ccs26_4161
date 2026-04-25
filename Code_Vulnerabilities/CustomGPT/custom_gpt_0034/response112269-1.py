
import numpy as np
import matplotlib.pyplot as plt

# Sample data: Create some distinct solutions (lines)
x1 = np.linspace(0, 10, 100)
y1 = 0.5 * x1 + np.random.normal(0, 1, size=x1.shape)  # Line 1

x2 = np.linspace(0, 10, 100)
y2 = -0.5 * x2 + np.random.normal(0, 1, size=x2.shape)  # Line 2

# Create the plot
plt.figure(figsize=(8, 6))

# Plot each line with varying opacity
plt.plot(x1, y1, color='blue', alpha=0.3)   # Line 1 with opacity
plt.plot(x2, y2, color='red', alpha=0.3)    # Line 2 with opacity

# Add more lines if needed
for i in range(3, 6):
    y = np.sin(x1 + i) + np.random.normal(0, 0.5, size=x1.shape)
    plt.plot(x1, y, alpha=0.3)  # Example line with random noise

# Customize the plot
plt.title('2D Density Plot of Distinct Solutions')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.xlim(0, 10)
plt.ylim(-5, 10)
plt.grid(True)

# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct lines in the parameter space
x1 = np.linspace(0, 10, 100)
y1 = 0.5 * x1 + np.random.normal(0, 0.5, size=x1.shape)

x2 = np.linspace(0, 10, 100)
y2 = -0.5 * x2 + np.random.normal(0, 0.5, size=x2.shape)

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity based on some probability (here, using a constant for illustration)
opacities = [0.3, 0.6]  # Example opacities for each line
plt.plot(x1, y1, color='blue', alpha=opacities[0], linewidth=2)
plt.plot(x2, y2, color='red', alpha=opacities[1], linewidth=2)

# Create an opacity overlay to enhance the blending effect
for i in range(100):
    plt.plot(x1, y1, color='blue', alpha=0.05)
    plt.plot(x2, y2, color='red', alpha=0.05)

# Set axis labels and title
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.title('2D Density Plot with Distinct Lines')
plt.grid(True)
plt.xlim([0, 10])
plt.ylim([-6, 6])
plt.show()

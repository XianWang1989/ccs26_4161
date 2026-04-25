
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct lines in parameter space
x = np.linspace(0, 10, 100)
lines = [np.sin(x + i) + i for i in np.linspace(0, 5, 10)]
probabilities = np.linspace(0.1, 1, len(lines))

# Create a figure
plt.figure(figsize=(8, 6))

# Plot each line with varying opacity
for line, prob in zip(lines, probabilities):
    plt.plot(x, line, color='b', alpha=prob, lw=2)

# Set plot limits and labels
plt.xlim(0, 10)
plt.ylim(-5, 5)
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')

# Display the plot
plt.grid()
plt.show()

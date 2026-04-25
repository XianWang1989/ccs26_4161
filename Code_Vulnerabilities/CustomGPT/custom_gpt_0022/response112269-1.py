
import numpy as np
import matplotlib.pyplot as plt

# Sample data generation
np.random.seed(0)
num_samples = 100
x = np.linspace(-3, 3, num_samples)
lines = [x, x**2 - 2, np.sin(x * 2) + 1]

# Corresponding probabilities for each line
probabilities = [0.3, 0.5, 0.2]

# Create a figure and axis
plt.figure(figsize=(8, 6))

# Plot each line with opacity corresponding to its probability
for line, prob in zip(lines, probabilities):
    plt.plot(x, line, alpha=prob, lw=2)

# Configure plot aesthetics
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Density Plot with Distinct Lines')
plt.grid(True)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')

# Show the plot
plt.show()

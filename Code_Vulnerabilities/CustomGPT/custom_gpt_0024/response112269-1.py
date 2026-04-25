
import numpy as np
import matplotlib.pyplot as plt

# Sample data representing distinct solutions
x = np.linspace(0, 10, 100)
lines = [np.sin(x + phase) + phase for phase in np.linspace(0, 2 * np.pi, 5)]
probabilities = np.random.rand(5)  # Assign random probabilities for line opacity

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each line with opacity based on probabilities
for line, prob in zip(lines, probabilities):
    plt.plot(x, line, alpha=prob, linewidth=2)

# Set plot attributes
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(-3, 3)

# Show plot
plt.show()

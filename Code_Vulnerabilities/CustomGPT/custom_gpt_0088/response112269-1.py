
import matplotlib.pyplot as plt
import numpy as np

# Sample data: create lines in 2D space
lines = [np.array([[x, np.sin(x + i)] for x in np.linspace(0, 10, 100)]) for i in range(5)]
probabilities = np.linspace(0.1, 1, len(lines))  # Example probabilities

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity
for line, prob in zip(lines, probabilities):
    plt.plot(line[:, 0], line[:, 1], alpha=prob, lw=2)

# Enhance appearance
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid()
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# Show the plot
plt.show()

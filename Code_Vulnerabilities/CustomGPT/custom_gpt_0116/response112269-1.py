
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data representing distinct solutions
num_lines = 10
x = np.linspace(0, 10, 100)

# Create random lines with different slopes and intercepts
solutions = [0.5 * i * x + np.random.normal(scale=0.5, size=x.shape) for i in range(1, num_lines + 1)]

# Create a density array to accumulate probabilities
density = np.zeros_like(x)

# Plot each distinct solution with opacity proportional to its probability
for line in solutions:
    # Normalize the line to a probability scale (0 to 1)
    prob = np.clip((line - np.min(line)) / (np.max(line) - np.min(line)), 0, 1)

    # Update density
    density += prob

    # Plot the line with opacity based on probability
    plt.plot(x, line, alpha=prob, color='blue')

# Display the density in a different color
plt.fill_between(x, density, color='gray', alpha=0.5, label='Density')

# Customize plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter 1')
plt.ylabel('Parameter 2')
plt.legend()
plt.grid()
plt.show()

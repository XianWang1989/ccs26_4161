
import numpy as np
import matplotlib.pyplot as plt

# Example data: create distinct lines in parameter space
num_lines = 10
x = np.linspace(0, 10, 100)
solutions = [np.sin(x + i) + i for i in range(num_lines)]

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot each line with a varying alpha based on some probability
for i, solution in enumerate(solutions):
    probability = 1 - (i / num_lines)  # Example probability
    plt.plot(x, solution, alpha=probability, color='blue')

# Enhance visibility by adding grid and labels
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid()

# Show the plot
plt.show()

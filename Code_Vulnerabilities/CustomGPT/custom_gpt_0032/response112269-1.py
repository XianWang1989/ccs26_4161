
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data: distinct linear solutions
x = np.linspace(0, 10, 100)
solutions = [
    (x, 0.1 * x + np.random.normal(scale=0.5, size=x.shape)) for _ in range(10)
]

# Create a figure
plt.figure(figsize=(10, 6))

# Plot each solution with varying opacity
for i, (x_data, y_data) in enumerate(solutions):
    # Calculate a probability density (you can modify this logic accordingly)
    prob_density = np.exp(-((x_data - 5)**2 + (y_data - 5)**2) / 10)

    # Adjust alpha based on probability density
    alpha_value = prob_density / np.max(prob_density)  # Normalize
    plt.plot(x_data, y_data, alpha=alpha_value, linewidth=2, color='blue')

# Set labels and title
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X Parameter')
plt.ylabel('Y Parameter')
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(0, 10)

# Show the plot
plt.show()

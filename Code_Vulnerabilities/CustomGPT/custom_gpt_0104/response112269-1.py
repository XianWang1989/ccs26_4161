
import numpy as np
import matplotlib.pyplot as plt

# Sample data: Generate distinct solutions
x = np.linspace(0, 10, 100)

# Assume we have three distinct lines (solutions) with different probabilities
y1 = 0.5 * np.sin(x) + 5
y2 = 0.5 * np.cos(x) + 5
y3 = 0.5 * np.sin(x + np.pi/4) + 5

# Probabilities associated with each line (0.0 to 1.0)
probabilities = [0.2, 0.6, 0.8]

# Create a figure and an axis
plt.figure(figsize=(10, 6))

# Plot each line with its corresponding opacity
for y, p in zip([y1, y2, y3], probabilities):
    plt.plot(x, y, color='blue', alpha=p, linewidth=2)

# Optional: Add a grid and labels for better visualization
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)

# Show the plot
plt.show()

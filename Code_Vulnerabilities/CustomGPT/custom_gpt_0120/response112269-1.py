
import numpy as np
import matplotlib.pyplot as plt

# Sample data: lines in parameter space
np.random.seed(0)
x = np.linspace(0, 10, 100)
lines = [np.sin(x + i) + np.random.normal(0, 0.1, size=x.shape) for i in range(5)]

# Create a canvas to plot
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity based on a hypothetical probability
for line in lines:
    plt.plot(x, line, alpha=0.5)  # Adjust alpha for opacity

# Set labels and title
plt.title("2D Density Plot with Distinct Lines")
plt.xlabel("Parameter 1")
plt.ylabel("Parameter 2")
plt.xlim(0, 10)
plt.ylim(-2, 2)

# Show the plot
plt.grid()
plt.show()

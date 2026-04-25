
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct solutions forming lines
num_lines = 100
x = np.linspace(0, 10, 100)

# Generate distinct solutions (lines)
solutions = [x + np.random.normal(0, 0.5, size=x.shape) + i for i in range(num_lines)]

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity (alpha)
for i, solution in enumerate(solutions):
    plt.plot(x, solution, color='blue', alpha=0.05)  # Change alpha for blending effect

plt.title("2D Density Plot with Distinct Lines")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(-5, 15)

plt.show()

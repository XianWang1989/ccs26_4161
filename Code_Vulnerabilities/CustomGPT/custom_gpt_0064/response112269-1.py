
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data: distinct lines
def generate_lines(num_lines, points_per_line):
    lines = []
    for i in range(num_lines):
        x = np.linspace(0, 10, points_per_line)
        # Create a line with a slight slope difference
        y = 0.1 * i * x + np.random.normal(scale=0.5, size=points_per_line)
        lines.append((x, y))
    return lines

# Create the plot
plt.figure(figsize=(10, 6))
num_lines = 10
points_per_line = 100
lines = generate_lines(num_lines, points_per_line)

# Plot each line with varying alpha based on its index
for idx, (x, y) in enumerate(lines):
    alpha = (idx + 1) / num_lines  # dynamic opacity
    plt.plot(x, y, color='blue', alpha=alpha)

plt.title("2D Density Plot with Distinct Lines")
plt.xlabel("Parameter X")
plt.ylabel("Parameter Y")
plt.grid()
plt.show()

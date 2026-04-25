
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data representing distinct lines
def generate_lines(num_lines, line_length):
    for i in range(num_lines):
        x = np.linspace(0, 10, line_length)
        # Vary the slope and intercept for each line
        y = i * x / (num_lines - 1) + np.random.normal(scale=0.5, size=line_length)
        yield x, y

# Setup the plot
plt.figure(figsize=(10, 6))

# Number of distinct solutions
num_lines = 5
line_length = 100

# Plot each line with varying opacity
for x, y in generate_lines(num_lines, line_length):
    # Calculate probability (for opacity)
    probability = (1 / num_lines) * (1 + np.sin(np.linspace(0, 2 * np.pi, line_length)))
    plt.plot(x, y, alpha=probability.max() * 0.5, color='blue')

# Customize the plot
plt.title("2D Density Plot of Distinct Lines")
plt.xlabel("Parameter X")
plt.ylabel("Parameter Y")
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(0, 10)

# Show the plot
plt.show()

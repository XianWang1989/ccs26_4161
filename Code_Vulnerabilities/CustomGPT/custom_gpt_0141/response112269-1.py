
import numpy as np
import matplotlib.pyplot as plt

# Simulate line data
num_lines = 10
x = np.linspace(-10, 10, 200)

# Create some lines and their corresponding probabilities
lines = []
probabilities = []

for i in range(num_lines):
    # Each line is a linear function with some noise
    slope = np.random.uniform(-1, 1)  # Random slope
    intercept = np.random.uniform(-10, 10)  # Random intercept
    y = slope * x + intercept + np.random.normal(scale=0.5, size=x.shape)
    lines.append(y)
    probability = np.random.uniform(0.1, 1.0)  # Random probability for opacity
    probabilities.append(probability)

# Plotting
plt.figure(figsize=(10, 6))

# Set the color map for continuous lines
for line, prob in zip(lines, probabilities):
    plt.plot(x, line, alpha=prob, linewidth=2)

# Enhancing the plot
plt.title("Density Plot of Distinct Lines")
plt.xlabel("Parameter 1")
plt.ylabel("Parameter 2")
plt.grid(True)
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.tight_layout()

# Show the plot
plt.show()

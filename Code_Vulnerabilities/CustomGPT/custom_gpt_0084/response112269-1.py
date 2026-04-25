
import numpy as np
import matplotlib.pyplot as plt

# Example data: distinct lines as solutions in param space
num_lines = 10
x = np.linspace(0, 10, 100)
probabilities = np.linspace(0.1, 1, num_lines)  # Example probabilities

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot each distinct solution line
for i in range(num_lines):
    y = np.sin(x + i)  # Example line, change as necessary
    plt.plot(x, y, alpha=probabilities[i], lw=2, color='blue')

plt.title("Density Plot with Distinct Lines")
plt.xlabel("Parameter X")
plt.ylabel("Parameter Y")
plt.grid()
plt.xlim(0, 10)
plt.ylim(-2, 2)

# Show the plot
plt.show()

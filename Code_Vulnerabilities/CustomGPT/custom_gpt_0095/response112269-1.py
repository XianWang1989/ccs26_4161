
import numpy as np
import matplotlib.pyplot as plt

# Sample data: generate two distinct lines
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + 5 + np.random.normal(scale=0.1, size=x1.shape)

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) + 5 + np.random.normal(scale=0.1, size=x2.shape)

# Define probabilities (for demonstration purposes)
prob1 = np.linspace(0.1, 1, 100)
prob2 = np.linspace(1, 0.1, 100)

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot the first line with varying opacity
for i in range(len(x1) - 1):
    plt.plot(x1[i:i + 2], y1[i:i + 2], color='blue', alpha=prob1[i], linewidth=2)

# Plot the second line with varying opacity
for i in range(len(x2) - 1):
    plt.plot(x2[i:i + 2], y2[i:i + 2], color='red', alpha=prob2[i], linewidth=2)

# Customize the plot
plt.title("Density Plot with Distinct Lines")
plt.xlabel("Parameter 1")
plt.ylabel("Parameter 2")
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(True)
plt.show()

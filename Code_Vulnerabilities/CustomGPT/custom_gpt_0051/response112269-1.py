
import numpy as np
import matplotlib.pyplot as plt

# Define some sample lines with associated probabilities
lines = [
    (np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)), 0.8),  # Line 1 with opacity 0.8
    (np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100) + 1) + 1, 0.5),  # Line 2 with opacity 0.5
    (np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100) + 2) + 2, 0.3)   # Line 3 with opacity 0.3
]

# Create the plot
plt.figure(figsize=(8, 6))

for x, y, alpha in lines:
    plt.plot(x, y, alpha=alpha, linewidth=2)

# Add title and labels
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show grid
plt.grid(True)

# Save or show the plot
plt.show()

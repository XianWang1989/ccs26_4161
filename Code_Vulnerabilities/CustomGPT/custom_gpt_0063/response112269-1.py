
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data representing lines in parameter space
# Each line is represented by two arrays of x and y coordinates
lines = [
    (np.linspace(0, 10, 100), np.linspace(0, 5, 100)),  # Line 1
    (np.linspace(0, 10, 100), np.linspace(5, 10, 100)), # Line 2
    (np.linspace(0, 10, 100), np.linspace(2, 7, 100)),  # Line 3
]

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity based on a probability scale
for x, y in lines:
    plt.plot(x, y, color='blue', alpha=0.5, linewidth=2)

# Optional: Customize the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)

# Show the plot
plt.show()

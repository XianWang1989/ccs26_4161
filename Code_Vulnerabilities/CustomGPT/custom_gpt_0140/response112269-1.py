
import numpy as np
import matplotlib.pyplot as plt

# Sample data: lines defined by parameters
x_values = np.linspace(0, 10, 100)
lines = [np.sin(x_values + i) + (i * 0.5) for i in range(5)]  # Example distinct solutions

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot each line with opacity based on its order
for i, line in enumerate(lines):
    plt.plot(x_values, line, alpha=0.5/(i+1), label=f'Solution {i+1}')  # Adjust alpha for blending

# Customize the plot
plt.title('Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

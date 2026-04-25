
import numpy as np
import matplotlib.pyplot as plt

# Generate some example data
np.random.seed(0)
num_lines = 20
x = np.linspace(0, 10, 100)  # X values
y = [np.sin(x + i) + np.random.normal(scale=0.1, size=x.shape) for i in range(num_lines)]  # Distinct solutions

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each solution line with varying alpha values
for i, yi in enumerate(y):
    ax.plot(x, yi, alpha=0.1 + 0.9 * (i / num_lines), linewidth=2)  # Adjust alpha based on index

# Optional: Add a colorbar or title
ax.set_title('Density Plot of Distinct Solutions')
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')

plt.grid()
plt.show()

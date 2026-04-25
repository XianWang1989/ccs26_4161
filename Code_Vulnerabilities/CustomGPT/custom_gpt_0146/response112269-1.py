
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data: distinct solutions represented as lines
x = np.linspace(-10, 10, 100)
lines = [np.sin(x + shift) + shift for shift in np.linspace(0, 7, 5)]  # 5 distinct lines

# Create a density plot using fill_between and adjusting alpha for transparency
plt.figure(figsize=(10, 6))

# Define color and alpha levels
colors = plt.cm.viridis(np.linspace(0, 1, len(lines)))

# Plot each line
for i, line in enumerate(lines):
    plt.fill_between(x, line, alpha=0.5, color=colors[i])

# Set limits and labels
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

plt.show()

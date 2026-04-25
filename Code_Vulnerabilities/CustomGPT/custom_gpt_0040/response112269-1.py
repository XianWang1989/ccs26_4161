
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct lines in parameter space
num_lines = 20
x = np.linspace(0, 10, 100)
y = [np.sin(x + i) + 0.1 * i for i in range(num_lines)]  # Generate some lines

# Assume some probabilities for each line (0 to 1)
probabilities = np.random.rand(num_lines)

# Prepare line segments
lines = [[(x0, y0), (x1, y1)] for y0, i in zip(y, range(num_lines)) for x0, x1 in zip(x[:-1], x[1:])]
lc = LineCollection(lines, linewidths=2, cmap='viridis', alpha=0)
lc.set_array(probabilities)
lc.set_edgecolor('black')

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-2, 2)  # Adjust as needed
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.set_title('2D Parameter Space Density with Distinct Lines')

# Display color bar to indicate probabilities
plt.colorbar(lc, ax=ax, label='Probability')
plt.show()

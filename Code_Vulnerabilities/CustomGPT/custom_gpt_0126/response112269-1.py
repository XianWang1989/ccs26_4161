
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: create distinct solutions as lines
x = np.linspace(0, 10, 100)
lines = []

# Create multiple lines with different probabilities
for i in range(5):
    y = np.sin(x + i) + np.random.normal(0, 0.1, size=x.shape)
    lines.append(np.column_stack([x, y]))

# Create LineCollection from the lines
lc = LineCollection(lines, linewidths=2, alpha=0.5)

# Create figure and axis
fig, ax = plt.subplots()
ax.add_collection(lc)

# Set limits
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-3, 3)

# Add a colorbar
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(0, len(lines)))
sm.set_array([])
plt.colorbar(sm, ax=ax)

# Labels and title
plt.title('Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')

plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Example data: lines in 2D parameter space
lines = [
    np.array([[0, 1], [1, 2]]),
    np.array([[0, 2], [1, 3]]),
    np.array([[0, 1.5], [1, 1]]),
    # ... add more lines as needed
]
probabilities = [0.2, 0.5, 0.8]  # Example probabilities for opacity

# Create the figure and axis
fig, ax = plt.subplots()

# Create a color map based on probabilities
norm = Normalize(vmin=0, vmax=max(probabilities))
cmap = plt.get_cmap('viridis')

for line, prob in zip(lines, probabilities):
    # Convert probability to alpha for transparency effect
    color = cmap(norm(prob))
    ax.add_collection(LineCollection([line], color=color, linewidth=2, alpha=prob))

# Set limits and labels
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 3)
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')
ax.set_title('2D Density Plot with Distinct Lines')

# Show colorbar
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, ax=ax, label='Probability')

plt.grid()
plt.show()

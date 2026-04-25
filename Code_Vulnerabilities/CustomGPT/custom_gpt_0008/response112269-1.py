
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize

# Sample data: Create some distinct line solutions
lines = [np.array([[x, np.sin(x) + np.random.uniform(-0.1, 0.1)] for x in np.linspace(0, 10, 100)]) for _ in range(5)]
probabilities = np.random.rand(len(lines))  # Random probabilities for each line

# Create a figure and axis
fig, ax = plt.subplots()

# Normalize probabilities for alpha blending
norm = Normalize(0, max(probabilities))

# Create a LineCollection
lc = LineCollection(lines, cmap='viridis', norm=norm, linewidth=2)

# Set the line colors based on their probabilities
lc.set_array(probabilities)
lc.set_alpha(0.5)  # Set some transparency

# Add the collection to the axes
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('2D Density Plot with Distinct Lines')

# Show the plot
plt.colorbar(lc, ax=ax, label='Probability')
plt.show()

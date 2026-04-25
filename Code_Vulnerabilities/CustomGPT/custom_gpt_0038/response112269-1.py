
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data for distinct solutions
num_lines = 10
x = np.linspace(0, 10, 100)

# Create random line solutions with associated probabilities
solutions = [np.sin(x + i) for i in range(num_lines)]
probabilities = np.random.rand(num_lines)  # Random probabilities

# Prepare segments
segments = []
for i, solution in enumerate(solutions):
    segments.append(np.column_stack((x, solution)))

# Create a LineCollection
lc = LineCollection(segments, linewidths=2, array=probabilities, cmap='Blues', norm=plt.Normalize(0, 1))

# Create the plot
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale_view()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-1.5, 1.5)
ax.set_title('2D Density Plot with Distinct Lines')

plt.colorbar(lc, label='Probability')
plt.show()

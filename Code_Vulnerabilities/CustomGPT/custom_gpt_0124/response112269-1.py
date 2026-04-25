
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data (replace with your actual data)
num_lines = 50
x = np.linspace(0, 10, 100)
lines = [np.column_stack((x, np.sin(x) + np.random.uniform(-0.1, 0.1))) for _ in range(num_lines)]
probabilities = np.random.rand(num_lines)  # Random probabilities for demonstration

# Create a line collection
segments = np.array(lines)
norm = plt.Normalize(0, np.max(probabilities))
colors = plt.cm.viridis(norm(probabilities))

line_segments = LineCollection(segments, cmap='viridis', norm=norm, linewidth=2, alpha=0.5)

fig, ax = plt.subplots()
ax.add_collection(line_segments)

# Set limits
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-2, 2)

# Add a colorbar
cb = plt.colorbar(line_segments, ax=ax, orientation='vertical')
cb.set_label('Probability')

# Add labels and title
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.set_title('2D Density Plot with Distinct Lines')

plt.show()

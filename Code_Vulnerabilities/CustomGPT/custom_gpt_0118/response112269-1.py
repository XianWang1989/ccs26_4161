
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path

# Generate some sample data
num_lines = 5
x = np.linspace(0, 10, 100)
probabilities = np.random.rand(num_lines)

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot each line with varying opacity
for i in range(num_lines):
    y = np.sin(x + i) + np.random.normal(scale=0.1, size=x.shape)
    # Create a path for the line
    line_path = Path(np.column_stack((x, y)))
    patch = PathPatch(line_path, facecolor='none', lw=2, alpha=probabilities[i])
    plt.gca().add_patch(patch)

# Set limits and labels
plt.xlim(0, 10)
plt.ylim(-3, 3)
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.grid()
plt.show()

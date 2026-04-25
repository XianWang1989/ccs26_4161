
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate sample data
num_lines = 10
x = np.linspace(0, 10, 100)
y = [np.sin(x + i) + np.random.normal(0, 0.1, x.shape) for i in range(num_lines)]

# Create line segments
points = np.array([[x[i], y_line[i]] for y_line in y for i in range(len(x))])
segments = np.array([points[i:i+2] for i in range(0, len(points)-1, 2)])

# Create a LineCollection with colors based on y-values
line_collection = LineCollection(segments, cmap='viridis', norm=plt.Normalize(0, num_lines),
                                 linewidths=2, alpha=0.5)

# Create a figure and axis
fig, ax = plt.subplots()

# Add the line collection to the axis
line_collection.set_array(np.arange(num_lines))
ax.add_collection(line_collection)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title('Density Plot of Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Show colorbar
plt.colorbar(line_collection, label='Probability')

# Display the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Generate synthetic data for distinct lines
# Let's create three different lines with distinct probabilities
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + np.random.normal(scale=0.1, size=x1.shape)

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) + np.random.normal(scale=0.1, size=x2.shape)

x3 = np.linspace(0, 10, 100)
y3 = np.tan(x3 * 0.1) + np.random.normal(scale=0.1, size=x3.shape)

# Combine the lines into a single array for LineCollection
lines = np.array([[x1, y1], [x2, y2], [x3, y3]])

# Create a LineCollection from the lines and set the colors and line widths based on probability/intensity
probabilities = [0.5, 0.8, 0.3]  # Example probabilities for each line
colors = [plt.cm.viridis(p) for p in probabilities]  # Map probabilities to colors

# Create segments for LineCollection
segments = np.array([np.column_stack([line[0], line[1]]) for line in lines])

# Create the LineCollection with specified linewidths and colors
lc = LineCollection(segments, colors=colors, linewidths=2)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.add_collection(lc)

# Set limits and labels
ax.set_xlim(0, 10)
ax.set_ylim(-3, 3)
ax.set_title("Density Plot of Distinct Solutions")
ax.set_xlabel("Parameter X")
ax.set_ylabel("Parameter Y")

# Display the plot
plt.colorbar(lc, ax=ax, label='Probability')
plt.show()

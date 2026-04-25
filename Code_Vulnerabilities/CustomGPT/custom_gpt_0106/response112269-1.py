
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct solutions represented as lines in 2D space
x_values = np.linspace(0, 10, 100)
line_probs = [0.1, 0.3, 0.5, 0.8]
lines = [np.sin(x_values + i) + i for i in range(len(line_probs))]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot each line with varying opacity
for i, line in enumerate(lines):
    ax.plot(x_values, line, alpha=line_probs[i], linewidth=2, label=f'Line {i+1} (p={line_probs[i]})')

# Add title and labels
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

# Adjust axes limits if necessary
ax.set_ylim(-2, 5)

# Show the plot
plt.grid()
plt.show()

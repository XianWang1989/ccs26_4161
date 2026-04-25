
import numpy as np
import matplotlib.pyplot as plt

# Sample data for three distinct lines
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + 5

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) + 5

x3 = np.linspace(0, 10, 100)
y3 = 0.5 * np.sin(x3) + 7

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Define a function to plot lines with opacity
def plot_line_with_opacity(x, y, alpha):
    ax.plot(x, y, alpha=alpha)

# Plot each line with varying opacity
plot_line_with_opacity(x1, y1, alpha=0.5)
plot_line_with_opacity(x2, y2, alpha=0.5)
plot_line_with_opacity(x3, y3, alpha=0.5)

# Set labels and title
ax.set_xlabel('Parameter X')
ax.set_ylabel('Parameter Y')
ax.set_title('2D Density Plot with Distinct Lines')

# Show the plot
plt.grid()
plt.show()

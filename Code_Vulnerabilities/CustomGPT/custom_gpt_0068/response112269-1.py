
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data: distinct lines in parameter space
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(scale=0.1, size=x.shape) + 1  # Line 1
y2 = np.cos(x) + np.random.normal(scale=0.1, size=x.shape) + 1.5  # Line 2
y3 = (np.sin(x) + np.cos(x)) / 2 + np.random.normal(scale=0.1, size=x.shape) + 2  # Line 3

# Combine the data into a single 2D array
lines = [y1, y2, y3]
colors = ['blue', 'orange', 'green']

# Plotting the density plot with line blending
plt.figure(figsize=(10, 6))

for line, color in zip(lines, colors):
    # Calculate the density and plot with alpha for blending
    density = np.exp(- (x[:, None] - line)**2 / (2 * 0.1**2))  # Gaussian density
    plt.fill_between(x, 0, density.mean(axis=0), color=color, alpha=0.5)

# Finalizing the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Density')
plt.grid()
plt.show()

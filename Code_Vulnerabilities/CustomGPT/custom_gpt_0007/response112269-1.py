
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data for distinct lines
x = np.linspace(-5, 5, 100)
y1 = 0.5 * x + 1
y2 = -0.25 * x + 1
y3 = np.sin(x) + 2
lines = [y1, y2, y3]

# Create a grid for density calculation
X, Y = np.meshgrid(x, np.linspace(-5, 5, 100))
Z = np.zeros_like(X)

# Add the contribution of each line to the density
for line in lines:
    # To simulate a density effect, use a Gaussian function centered around each line
    for i in range(len(x)):
        Z += np.exp(-0.5 * ((Y - line[i]) ** 2) / 0.1)  # Adjust the variance as needed

# Normalize the density
Z /= np.max(Z)

# Plotting
plt.figure(figsize=(10, 6))
plt.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.5)  # Base density plot
for i, line in enumerate(lines):
    plt.plot(x, line, color='red', linewidth=2, alpha=0.7)  # Overlay distinct lines

plt.title('2D Density Plot with Distinct Solutions')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.colorbar(label='Density')
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Generate sample data (distinct lines)
x = np.linspace(-5, 5, 100)
y1 = np.exp(-x**2) * np.sin(2 * np.pi * x) + 1  # Distinct line 1
y2 = np.exp(-x**2) * np.cos(2 * np.pi * x) - 1  # Distinct line 2

# Probability associated with each line (opacity)
prob1 = 0.7
prob2 = 0.5

plt.figure(figsize=(10, 6))

# Plot lines with opacity
plt.plot(x, y1, color='blue', alpha=prob1, lw=2, label='Solution 1')
plt.plot(x, y2, color='red', alpha=prob2, lw=2, label='Solution 2')

# Fill between lines to visualize density
plt.fill_between(x, y1, y2, where=(y1 > y2), color='blue', alpha=0.1)
plt.fill_between(x, y1, y2, where=(y1 < y2), color='red', alpha=0.1)

# Styling the plot
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.legend()
plt.grid()

plt.show()

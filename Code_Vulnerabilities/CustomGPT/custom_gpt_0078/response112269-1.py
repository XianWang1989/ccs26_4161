
import numpy as np
import matplotlib.pyplot as plt

# Sample data: generating distinct lines in the parameter space
num_lines = 100
x = np.linspace(0, 10, 100)

# Create distinct lines with different probabilities
y1 = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)
y2 = np.cos(x) + np.random.normal(0, 0.1, size=x.shape)
y3 = np.sin(2 * x) + np.random.normal(0, 0.1, size=x.shape)

# Calculate probabilities (just as an example, can be more complex)
prob1 = np.exp(-0.1 * (y1 - 5)**2)
prob2 = np.exp(-0.1 * (y2 - 5)**2)
prob3 = np.exp(-0.1 * (y3 - 5)**2)

# Normalize probabilities
prob1 /= prob1.max()
prob2 /= prob2.max()
prob3 /= prob3.max()

# Plotting
plt.figure(figsize=(10, 6))

# Use alpha to blend lines based on probability
plt.plot(x, y1, color='blue', alpha=prob1, lw=2, label='Solution 1')
plt.plot(x, y2, color='orange', alpha=prob2, lw=2, label='Solution 2')
plt.plot(x, y3, color='green', alpha=prob3, lw=2, label='Solution 3')

# Optionally, fill under the lines to visualize density
plt.fill_between(x, y1, alpha=0.1, color='blue')
plt.fill_between(x, y2, alpha=0.1, color='orange')
plt.fill_between(x, y3, alpha=0.1, color='green')

plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()

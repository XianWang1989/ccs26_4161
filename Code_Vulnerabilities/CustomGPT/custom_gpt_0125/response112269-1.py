
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct lines in a parameter space
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1) + 1
opacity1 = 0.5

x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2) + 1
opacity2 = 0.3

plt.figure(figsize=(10, 6))
plt.plot(x1, y1, color='blue', alpha=opacity1, label='Solution 1')
plt.plot(x2, y2, color='red', alpha=opacity2, label='Solution 2')

# Adjust the limits and labels
plt.xlim(0, 10)
plt.ylim(0, 3)
plt.xlabel('Parameter 1')
plt.ylabel('Parameter 2')
plt.title('Density Plot with Distinct Lines')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

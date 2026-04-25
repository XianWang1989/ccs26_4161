
import numpy as np
import matplotlib.pyplot as plt

# Sample data: lines in parameter space
lines = [
    (np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)), 0.5),   # Line 1
    (np.linspace(0, 10, 100), np.cos(np.linspace(0, 10, 100)), 0.3),   # Line 2
    (np.linspace(0, 10, 100), np.linspace(0, 10, 100), 0.7)            # Line 3
]

plt.figure(figsize=(8, 6))

for x, y, prob in lines:
    plt.plot(x, y, alpha=prob, linewidth=2)

plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter 1')
plt.ylabel('Parameter 2')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(True)
plt.show()

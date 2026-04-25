
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct solutions in 2D parameter space
num_lines = 100
x = np.linspace(0, 10, 100)

# Generating distinct lines with random slopes and intercepts
lines = []
probabilities = []

for _ in range(num_lines):
    slope = np.random.uniform(-1, 1)
    intercept = np.random.uniform(0, 10)
    y = slope * x + intercept
    opacity = np.random.uniform(0.1, 1.0)
    lines.append((x, y, opacity))

# Create a LineCollection
segments = []
for x_vals, y_vals, alpha in lines:
    segments.append(np.array([x_vals, y_vals]).T)

# Convert to LineCollection
lc = LineCollection(np.concatenate(segments), array=np.array([alpha for _, _, alpha in lines]),
                    linewidths=2, cmap='viridis', alpha=0.5)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.add_collection(lc)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')

plt.colorbar(lc, label='Opacity (Probability)')
plt.show()

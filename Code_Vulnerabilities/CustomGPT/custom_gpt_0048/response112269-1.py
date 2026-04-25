
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize

# Example data: Distinct solutions
lines = [
    (np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)) + i) for i in range(5)
]

# Corresponding probabilities (for alpha blending)
probabilities = np.random.rand(len(lines))

# Create a figure
fig, ax = plt.subplots(figsize=(8, 6))

# Normalize probabilities for opacity
norm = Normalize(vmin=0, vmax=max(probabilities))
colors = plt.cm.viridis(norm(probabilities))

# Plot each line with corresponding opacity
for idx, (x, y) in enumerate(lines):
    ax.plot(x, y, color=colors[idx], alpha=probabilities[idx], lw=2)

# Optional: Use a density overlay
# Create a grid and calculate density if needed
# [This part may vary if you decide to add a density overlay]

plt.title("Density Plot of Distinct Lines")
plt.xlabel("Parameter X")
plt.ylabel("Parameter Y")
plt.grid()
plt.show()

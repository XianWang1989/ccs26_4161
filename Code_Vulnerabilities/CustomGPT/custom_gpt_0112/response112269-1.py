
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: list of lines (x1, y1, x2, y2) and their probabilities
lines = [
    (0, 0, 5, 5, 0.8),
    (1, 4, 4, 1, 0.5),
    (2, 1, 3, 2, 0.9),
    (0, 3, 3, 0, 0.6),
]

# Create an array of segments and their associated probabilities
segments = np.array([[x1, y1, x2, y2] for x1, y1, x2, y2, _ in lines])
probabilities = np.array([p for _, _, _, _, p in lines])

# Create a LineCollection
lc = LineCollection(segments[:, None, :], cmap='viridis', linestyle='-', linewidths=4)

# Set the alpha based on probabilities
lc.set_array(probabilities)
lc.set_norm(plt.Normalize(0, 1))  # Normalize probabilities between 0 and 1

# Plotting
plt.figure(figsize=(8, 6))
plt.gca().add_collection(lc)
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.colorbar(lc, label='Probability')
plt.xlabel('Parameter 1')
plt.ylabel('Parameter 2')
plt.title('2D Density Plot with Distinct Lines')
plt.grid()
plt.show()

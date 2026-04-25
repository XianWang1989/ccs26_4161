
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Example data: lines in parameter space with associated probabilities
lines = [np.array([[0, 0], [1, 1]]), 
         np.array([[0, 1], [1, 0]]), 
         np.array([[0, 0], [1, 0.5]])]
probabilities = [0.8, 0.6, 0.7]

# Prepare line segments
segments = np.concatenate([line[:, None, :] for line in lines])
lc = LineCollection(segments, linewidths=2, cmap='viridis')

# Normalize probabilities to [0, 1] for alpha blending
norm_probs = (np.array(probabilities) - min(probabilities)) / (max(probabilities) - min(probabilities))
lc.set_array(norm_probs)
lc.set_array(norm_probs)

# Create a figure
fig, ax = plt.subplots()
ax.add_collection(lc)

# Set limits
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)

# Add colorbar, showing the probability scale
cbar = plt.colorbar(lc, ax=ax, label='Probability')
cbar.set_ticks([0, 0.5, 1])
cbar.set_ticklabels(['Low', 'Medium', 'High'])

plt.title('Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid()
plt.show()

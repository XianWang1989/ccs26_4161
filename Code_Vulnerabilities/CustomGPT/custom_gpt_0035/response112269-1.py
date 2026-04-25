
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Sample data: distinct solutions in 2D
x = np.linspace(-5, 5, 100)
y1 = 0.5*x + 2
y2 = -0.5*x + 2
y3 = np.sin(x) + 1

# Probability values for each line
probabilities = np.array([0.2, 0.5, 0.8])  # Different probabilities

# Create list of line segments with opacities set by probability
lines = [
    np.array([[x[i], y1[i]] for i in range(len(x))]),
    np.array([[x[i], y2[i]] for i in range(len(x))]),
    np.array([[x[i], y3[i]] for i in range(len(x))]),
]

# Create LineCollection
lc = LineCollection(lines, linewidths=2, cmap='Blues', alpha=0)
for line, prob in zip(lines, probabilities):
    lc.set_array(np.array([prob]))
    lc.set_alpha(prob)  # Set opacity based on probability

# Plot
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale_view()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_title('Density Plot with Distinct Lines')
plt.colorbar(lc, label='Probability')
plt.show()

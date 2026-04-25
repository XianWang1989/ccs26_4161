
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Sample distinct solutions represented as (x, y) tuples
solutions = [
    np.random.normal(loc=(1, 1), scale=0.05, size=(100, 2)),
    np.random.normal(loc=(2, 2), scale=0.05, size=(100, 2)),
    np.random.normal(loc=(3, 1), scale=0.05, size=(100, 2))
]

# Prepare the KDE
x_coords = np.concatenate([sol[:, 0] for sol in solutions])
y_coords = np.concatenate([sol[:, 1] for sol in solutions])
kde = gaussian_kde(np.vstack([x_coords, y_coords]))

# Generate grid for plotting
x_grid = np.linspace(0, 4, 100)
y_grid = np.linspace(0, 3, 100)
X, Y = np.meshgrid(x_grid, y_grid)
Z = kde(np.vstack([X.ravel(), Y.ravel()])).reshape(X.shape)

# Plot the density
plt.imshow(Z, aspect='auto', extent=(0, 4, 0, 3), origin='lower', cmap='Blues', alpha=0.5)

# Plot each distinct solution with probability-based opacity
for i, solution in enumerate(solutions):
    # Estimate the density along the line
    density = kde(solution.T)
    # Normalize density for opacity
    opacity = density / density.max()
    plt.plot(solution[:, 0], solution[:, 1], color=(1, 0, 0, 0.5 * opacity), linewidth=2)

plt.colorbar(label='Density')
plt.xlim(0, 4)
plt.ylim(0, 3)
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.title('Density Plot with Distinct Lines')
plt.show()

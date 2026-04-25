
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters
f_wid = 5  # Filter width (size)
sigma = 1.0  # Standard deviation (sigma)

# Create a 5x5 grid
size = f_wid
x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

# Compute the Gaussian function
g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
g /= g.sum()  # Normalize the filter

print(g)

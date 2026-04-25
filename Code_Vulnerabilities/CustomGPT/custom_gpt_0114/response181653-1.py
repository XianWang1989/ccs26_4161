
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters
size = 5
sigma = 1.0  # Adjust sigma for different spread of the Gaussian

# Create an empty array
filter_size = (size, size)
gaussian_filter_5x5 = np.zeros(filter_size)

# Create a 5x5 Gaussian filter
for x in range(size):
    for y in range(size):
        gaussian_filter_5x5[x, y] = (
            (1 / (2 * np.pi * sigma**2)) * 
            np.exp(-((x - (size // 2))**2 + (y - (size // 2))**2) / (2 * sigma**2))
        )

# Normalize the filter
gaussian_filter_5x5 /= np.sum(gaussian_filter_5x5)

print(gaussian_filter_5x5)

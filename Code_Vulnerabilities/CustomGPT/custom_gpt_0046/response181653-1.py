
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation

# Create an empty array
filter_size = (size, size)
gaussian_filter = np.zeros(filter_size)

# Generate Gaussian filter
for x in range(size):
    for y in range(size):
        gaussian_filter[x, y] = (1/(2 * np.pi * sigma ** 2)) * np.exp(-((x - (size // 2)) ** 2 + (y - (size // 2)) ** 2) / (2 * sigma ** 2))

# Normalize the filter
gaussian_filter /= np.sum(gaussian_filter)

print(gaussian_filter)

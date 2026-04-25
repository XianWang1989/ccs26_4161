
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters
size = 5  # Size of the filter (5x5)
sigma = 1  # Standard deviation for Gaussian

# Create the Gaussian filter
gaussian_kernel = np.zeros((size, size))
for x in range(size):
    for y in range(size):
        gaussian_kernel[x, y] = (1/(2 * np.pi * sigma**2)) * np.exp(-((x - (size-1)/2)**2 + (y - (size-1)/2)**2) / (2 * sigma**2))

# Normalize the kernel
gaussian_kernel /= np.sum(gaussian_kernel)

# Print the Gaussian filter
print(gaussian_kernel)

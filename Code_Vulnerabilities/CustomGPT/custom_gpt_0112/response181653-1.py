
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters for the Gaussian filter
size = 5  # Size of the filter
sigma = 1  # Standard deviation

# Create an array of zeros
filter_array = np.zeros((size, size))

# Create the filter using a Gaussian function
for x in range(size):
    for y in range(size):
        filter_array[x, y] = np.exp(-((x - size // 2) ** 2 + (y - size // 2) ** 2) / (2 * sigma ** 2))

# Normalize the filter to sum to 1
filter_array /= 2 * np.pi * sigma ** 2
filter_array /= filter_array.sum()

print(filter_array)

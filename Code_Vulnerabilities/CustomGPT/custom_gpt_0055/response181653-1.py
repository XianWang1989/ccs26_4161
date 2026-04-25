
import numpy as np
from scipy.ndimage import gaussian_filter

# Define parameters for the Gaussian filter
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation for the Gaussian

# Create the Gaussian filter
gaussian_filter_matrix = np.zeros((size, size))

for i in range(size):
    for j in range(size):
        x = i - (size - 1) / 2
        y = j - (size - 1) / 2
        gaussian_filter_matrix[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2))

# Normalize the filter
gaussian_filter_matrix /= np.sum(gaussian_filter_matrix)

print(gaussian_filter_matrix)

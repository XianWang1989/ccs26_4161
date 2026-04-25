
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    # Create an empty array
    filter_size = (size, size)

    # Create a Gaussian filter using the scipy gaussian_filter
    gaussian_filter_matrix = np.zeros(filter_size)

    # Center of the filter
    center = (size // 2, size // 2)

    for x in range(size):
        for y in range(size):
            gaussian_filter_matrix[x, y] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(-((x - center[0]) ** 2 + (y - center[1]) ** 2) / (2 * sigma ** 2))

    # Normalize the filter
    gaussian_filter_matrix /= np.sum(gaussian_filter_matrix)

    return gaussian_filter_matrix

# Example usage
size = 5
sigma = 1.0
gaussian_filter_5x5 = create_gaussian_filter(size, sigma)
print(gaussian_filter_5x5)

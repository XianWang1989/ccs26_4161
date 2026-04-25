
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size=5, sigma=1):
    # Create an empty filter
    filter_size = size
    GaussianFilter = np.zeros((filter_size, filter_size))

    # Calculate the center point
    center = filter_size // 2

    # Generate a Gaussian filter
    for x in range(filter_size):
        for y in range(filter_size):
            GaussianFilter[x, y] = (
                1 / (2 * np.pi * sigma ** 2) *
                np.exp(-((x - center) ** 2 + (y - center) ** 2) / (2 * sigma ** 2))
            )

    # Normalize to ensure the sum is 1
    return GaussianFilter / np.sum(GaussianFilter)

# Usage
gaussian_filter = create_gaussian_filter(size=5, sigma=1)
print(gaussian_filter)

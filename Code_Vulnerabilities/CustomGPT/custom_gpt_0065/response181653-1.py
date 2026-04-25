
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1.0):
    """Create a Gaussian filter."""
    # Create an empty array
    filter_array = np.zeros((size, size), dtype=np.float32)

    # Calculate the center of the filter
    center = size // 2

    # Fill the filter
    for x in range(size):
        for y in range(size):
            filter_array[x, y] = np.exp(-((x - center) ** 2 + (y - center) ** 2) / (2 * sigma ** 2))

    # Normalize the filter
    filter_array /= np.sum(filter_array)
    return filter_array

# Generate a Gaussian filter
gaussian_filter_5x5 = gaussian_filter(size=5, sigma=1.0)
print(gaussian_filter_5x5)

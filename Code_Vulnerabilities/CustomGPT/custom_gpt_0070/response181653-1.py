
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_5x5(sigma):
    # Create a 5x5 grid
    size = 5
    # Create an array with a single element
    array = np.zeros((size, size))
    # Use gaussian_filter to create a Gaussian kernel
    array = gaussian_filter(array, sigma=sigma, truncate=2.0)

    # Normalize the filter
    return array / np.sum(array)

# Example usage
sigma = 1.0  # Standard deviation
filter_5x5 = gaussian_filter_5x5(sigma)

print(filter_5x5)

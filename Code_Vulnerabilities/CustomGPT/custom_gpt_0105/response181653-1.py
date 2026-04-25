
import numpy as np

def gaussian_filter(size, sigma):
    """Creates a Gaussian filter of given size and standard deviation (sigma)."""
    # Create a grid of (x, y) coordinates
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2.0 * sigma**2))
    g /= g.sum()  # Normalize the filter

    return g

# Parameters
size = 5  # Filter size
sigma = 1.0  # Standard deviation

# Generate the filter
gaussian_filter_matrix = gaussian_filter(size, sigma)
print(gaussian_filter_matrix)

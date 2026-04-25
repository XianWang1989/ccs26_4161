
import numpy as np

def gaussian_filter(size, sigma):
    """Create a Gaussian filter."""
    # Create a grid of (x, y) coordinates
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2.0 * sigma**2))

    # Normalize the filter
    return g / g.sum()

# Parameters for a Gaussian filter
size = 5  # Size of the filter (5x5)
sigma = 1  # Standard deviation (can be adjusted)

# Create the Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)

print(gaussian_kernel)

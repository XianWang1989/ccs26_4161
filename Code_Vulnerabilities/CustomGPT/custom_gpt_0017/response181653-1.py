
import numpy as np

def gaussian_filter(size, sigma):
    """Generate a Gaussian filter."""
    # Create a grid of (x, y) coordinates
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter
    return g / g.sum()

# Parameters
size = 5  # Filter size (5x5)
sigma = 1.0  # Standard deviation

# Generate Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)

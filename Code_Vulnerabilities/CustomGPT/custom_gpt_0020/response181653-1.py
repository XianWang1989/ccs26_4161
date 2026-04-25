
import numpy as np

def gaussian_filter(size, sigma):
    # Create a 5x5 grid of (x, y) coordinates
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the Gaussian kernel to ensure the sum is 1
    return g / g.sum()

# Parameters for the filter
filter_size = 5
sigma = 1.0  # Standard deviation

# Create the Gaussian filter
gaussian_kernel = gaussian_filter(filter_size, sigma)

print(gaussian_kernel)

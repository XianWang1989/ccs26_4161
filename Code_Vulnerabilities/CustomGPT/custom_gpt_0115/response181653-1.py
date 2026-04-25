
import numpy as np

def gaussian_filter(size, sigma):
    """Generate a Gaussian filter."""
    # Create a 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    return g / np.sum(g)  # Normalize to make the sum equal to 1

# Set parameters
size = 5
sigma = 1.0

# Generate Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)

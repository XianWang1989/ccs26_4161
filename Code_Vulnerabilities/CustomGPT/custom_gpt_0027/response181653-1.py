
import numpy as np

def gaussian_filter(size, sigma):
    """Generate a Gaussian filter."""
    if size % 2 == 0:
        size += 1  # Ensure size is odd

    # Create a grid of (x, y) coordinates
    ax = np.arange(-(size // 2), size // 2 + 1)
    xx, yy = np.meshgrid(ax, ax)

    # Calculate the Gaussian function
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / g.sum()  # Normalize the filter

# Example usage
size = 5
sigma = 1.0
gaussian_filter_5x5 = gaussian_filter(size, sigma)
print(gaussian_filter_5x5)

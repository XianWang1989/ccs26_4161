
import numpy as np

def gaussian_filter(size, sigma):
    """Create a Gaussian filter."""
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / np.sum(g)  # Normalize

# Parameters
size = 5  # 5x5 filter
sigma = 1.0  # Standard deviation

# Generate Gaussian filter
filter_ = gaussian_filter(size, sigma)

print(filter_)

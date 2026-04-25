
import numpy as np

def gaussian_filter(size: int, sigma: float) -> np.ndarray:
    """Generate a Gaussian filter."""
    ax = np.linspace(-(size // 2), size // 2, size)
    x, y = np.meshgrid(ax, ax)
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / g.sum()  # Normalize the filter

# Parameters
size = 5  # Filter size (5x5)
sigma = 1.0  # Standard deviation

# Create Gaussian filter
gaussian = gaussian_filter(size, sigma)
print(gaussian)

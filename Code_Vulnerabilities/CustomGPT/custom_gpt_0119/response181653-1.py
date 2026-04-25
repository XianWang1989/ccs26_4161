
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size=5, sigma=1):
    # Create a 5x5 grid
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)

    # Calculate the Gaussian function
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))

    # Normalize to ensure the sum of coefficients is 1
    g /= np.sum(g)
    return g

# Example usage
gaussian_filter = create_gaussian_filter(size=5, sigma=1)
print(gaussian_filter)

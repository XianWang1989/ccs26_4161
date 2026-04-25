
import numpy as np

def gaussian_filter(size=5, sigma=1.0):
    """Generates a Gaussian filter."""
    # Create a grid of (x,y) coordinates
    x = np.linspace(-size // 2 + 1, size // 2, size)
    y = np.linspace(-size // 2 + 1, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma ** 2))

    # Normalize the filter
    return g / g.sum()

# Create a Gaussian filter of size 5x5
filter_5x5 = gaussian_filter(size=5, sigma=1.0)
print(filter_5x5)

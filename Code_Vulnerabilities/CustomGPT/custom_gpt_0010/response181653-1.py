
import numpy as np
import scipy.ndimage as ndimage

def gaussian_filter(size=5, sigma=1):
    # Create a grid of (x, y) coordinates
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the 2D Gaussian
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / (2 * np.pi * sigma**2)

# Generate the filter
filter_5x5 = gaussian_filter(size=5, sigma=1)

# Print the filter
print(np.round(filter_5x5, 7))  # Adjust precision as needed

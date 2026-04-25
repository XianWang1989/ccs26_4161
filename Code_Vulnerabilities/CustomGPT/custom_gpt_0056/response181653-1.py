
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size: int, sigma: float) -> np.ndarray:
    # Create a 2D grid of (x, y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter to sum to 1
    g /= g.sum()

    return g

# Parameters
filter_size = 2  # this will give a 5x5 filter (size 2 means range from -2 to 2)
sigma = 1.0

# Create the filter
gaussian_filter = create_gaussian_filter(filter_size, sigma)

print(gaussian_filter)

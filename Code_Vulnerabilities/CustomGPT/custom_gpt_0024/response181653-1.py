
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters for the Gaussian filter
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation

# Create a Gaussian filter
filter_size = (size, size)
x = np.linspace(-size // 2 + 1, size // 2, size)
y = np.linspace(-size // 2 + 1, size // 2, size)
x, y = np.meshgrid(x, y)
g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
g = g / (2 * np.pi * sigma**2)

# Display the Gaussian filter
print(g)

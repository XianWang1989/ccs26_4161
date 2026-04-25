
import numpy as np
import matplotlib.pyplot as plt

def gaussian_filter(size, sigma):
    """Creates a Gaussian filter."""
    # Create a grid of (x,y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the Gaussian filter
    g /= g.sum()

    return g

# Example parameters
size = 2  # filter size will be 5x5
sigma = 1.0  # standard deviation

# Create the filter
gaussian_kernel = gaussian_filter(size, sigma)

# Print the output
print(gaussian_kernel)

# Optional: Visualize the kernel
plt.imshow(gaussian_kernel, cmap='gray')
plt.colorbar()
plt.title('Gaussian Filter')
plt.show()

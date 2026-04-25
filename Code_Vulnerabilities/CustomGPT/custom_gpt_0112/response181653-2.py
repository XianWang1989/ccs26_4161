
from scipy.ndimage import gaussian_filter

# Create a flat array and apply Gaussian filter
flat_array = np.zeros((5, 5))
flat_array[2, 2] = 1  # Center peak

# Apply Gaussian filter
gaussian_filtered = gaussian_filter(flat_array, sigma=1)

print(gaussian_filtered)

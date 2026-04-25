
import numpy as np

# Create a 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the 2D array into a 3D array (300, 10000, 50)
# Ensure the total number of elements is compatible; 300 * 10000 * 50 = 15000000
# For our case, since we have 3000000 elements in 2D, we can directly reshape it
# Make sure to reshape correctly based on your needs
# Here we can reshape with (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verifying the new shape
print(reshaped_data.shape)  # Output: (300, 10000, 50)

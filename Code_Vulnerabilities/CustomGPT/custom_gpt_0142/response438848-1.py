
import numpy as np

# Generate a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data to (300, 10000, 50)
# Since 3000000 = 300 * 10000, this will work perfectly.
reshaped_data = data.reshape(300, 10000, 50)

# Verifying the shape of the new 3D array
print("Original shape:", data.shape)
print("Reshaped shape:", reshaped_data.shape)

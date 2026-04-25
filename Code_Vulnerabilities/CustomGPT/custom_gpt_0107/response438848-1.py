
import numpy as np

# Generate a random 2D array of size 3000000 x 50
data = np.random.randn(3000000, 50)

# Check the shape of the original data
print("Original shape:", data.shape)

# Reshape the data into a 3D array of size 300 x 10000 x 50
reshaped_data = data.reshape(300, 10000, 50)

# Check the shape of the reshaped data
print("Reshaped shape:", reshaped_data.shape)

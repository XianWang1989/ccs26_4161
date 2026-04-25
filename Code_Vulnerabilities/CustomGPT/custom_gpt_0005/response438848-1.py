
import numpy as np

# Generate a random 2D array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the 2D array into a 3D array of size (300, 10000, 50)
data_reshaped = data.reshape(300, 10000, 50)

# Print the shapes to verify
print("Original shape:", data.shape)
print("Reshaped shape:", data_reshaped.shape)

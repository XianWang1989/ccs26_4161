
import numpy as np

# Create a random 2D matrix of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
# New shape: (300, 10000, 50)
D_reshaped = data.reshape((300, 10000, 50))

# To verify the shape of the new array
print("Original shape:", data.shape)
print("New shape:", D_reshaped.shape)

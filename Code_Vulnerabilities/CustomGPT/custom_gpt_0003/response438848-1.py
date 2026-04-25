
import numpy as np

# Create a dummy 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the array into (300, 10000, 50)
data_3d = data.reshape(300, 10000, 50)

# Verify the shape of the new 3D array
print("Original shape:", data.shape)
print("New 3D shape:", data_3d.shape)  # Should output (300, 10000, 50)

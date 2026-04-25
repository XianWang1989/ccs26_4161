
import numpy as np

# Create a random 2D array of size 3000000 x 50
data = np.random.randn(3000000, 50)

# Reshape the array to the desired 3D shape
# 300 matrices of size 10000 x 50
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape
print(reshaped_data.shape)  # Should output (300, 10000, 50)

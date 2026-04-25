
import numpy as np

# Create a random 2D array of size 3000000x50
data = np.random.randn(3000000, 50)

# Reshape it into a 3D array of size (300, 10000, 50)
# This works because 300 * 10000 * 50 = 3000000 * 50
data_3d = data.reshape(300, 10000, 50)

# Verify the shape of the new 3D array
print("Shape of the original data:", data.shape)
print("Shape of the reshaped data:", data_3d.shape)


import numpy as np

# Generate a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array (300, 10000, 50)
# This works because 300 * 10000 * 50 = 3000000 * 50
data_3d = data.reshape((300, 10000, 50))

# Optionally, you can verify the shape of the new array
print(data_3d.shape)  # Should output: (300, 10000, 50)

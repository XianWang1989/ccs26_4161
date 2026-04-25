
import numpy as np

# Generate the 2D array
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
# 300 matrices of shape (10000, 50)
data_3d = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(data_3d.shape)  # Output should be (300, 10000, 50)


import numpy as np

# Create a sample 2D array of size 3000000 x 50
data = np.random.randn(3000000, 50)

# Reshape the data to the desired 3D shape
# The shape will be (300, 10000, 50) -> (number of matrices, number of rows per matrix, number of columns)
data_3d = data.reshape(300, 10000, 50)

# Display the shape of the new 3D array
print(data_3d.shape)  # Output should be (300, 10000, 50)


import numpy as np

# Create a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape into a 3D array of shape (300, 10000, 50)
# The first dimension represents the number of matrices,
# the second dimension represents the rows in each matrix,
# and the third dimension represents the columns.
data_3d = data.reshape(300, 10000, 50)

# Verify the shape of the new 3D array
print(data_3d.shape)

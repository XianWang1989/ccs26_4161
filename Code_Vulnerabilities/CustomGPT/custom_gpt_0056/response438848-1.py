
import numpy as np

# Create a random 2D array (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the 2D array into a 3D array
# The first dimension is the number of matrices (300),
# the second is the number of rows in each matrix (10000),
# and the third is the number of columns (50).
data_3d = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(data_3d.shape)  # Should output (300, 10000, 50)

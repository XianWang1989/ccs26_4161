
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Desired shape
num_matrices = 300
matrix_size = 10000

# Reshape the data into a 3D array
# Should reshape directly if data is in the correct shape
# (3000000, 50) can be reshaped to (300, 10000, 50)
reshaped_data = data.reshape(num_matrices, matrix_size, -1)

# Verify the shape of the new 3D array
print(reshaped_data.shape)  # Should output (300, 10000, 50)

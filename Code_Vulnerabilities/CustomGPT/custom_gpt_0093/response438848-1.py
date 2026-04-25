
import numpy as np

# Generate a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array of shape (300, 10000, 50)
# Here, we use the first dimension as the number of matrices
# The second dimension is the rows per matrix (10000)
# The third dimension is the columns (50)
reshaped_data = data.reshape(300, 10000, 50)

print(f'Original shape: {data.shape}')
print(f'Reshaped to 3D: {reshaped_data.shape}')

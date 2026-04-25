
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data
num_matrices = 300
rows_per_matrix = 10000
columns = 50

# Ensure the data can be reshaped correctly
reshaped_data = data.reshape(num_matrices, rows_per_matrix, columns)

# Verify the shape of the new array
print(reshaped_data.shape)  # Output: (300, 10000, 50)

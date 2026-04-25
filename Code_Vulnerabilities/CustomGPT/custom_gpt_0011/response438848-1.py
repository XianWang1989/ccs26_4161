
import numpy as np

# Create the original 2D array
data = np.random.randn(3000000, 50)

# The number of matrices and the shape of each matrix
num_matrices = 300
rows_per_matrix = 10000
columns = 50

# Reshape the data into a 3D array
# Ensure the original data size matches the new shape (3000000 = 300 * 10000)
if data.shape[0] == num_matrices * rows_per_matrix:
    result = data.reshape(num_matrices, rows_per_matrix, columns)
else:
    raise ValueError("The total elements do not match. Please check your input data dimensions.")

# Example usage
print("Shape of the resulting 3D array:", result.shape)  # Output should be (300, 10000, 50)

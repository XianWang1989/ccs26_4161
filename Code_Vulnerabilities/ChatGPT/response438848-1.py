
import numpy as np

# Create a sample 2D array with shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Desired shape: (300 matrices of shape (10000, 50))
num_matrices = 300  # Total number of matrices
window_length = 10000  # Size of each matrix
num_features = 50  # Number of features

# Reshape the data into 3D array
D = data.reshape(num_matrices, window_length, num_features)

# Print the shape to confirm
print(D.shape)  # Should be (300, 10000, 50)


import numpy as np

# Create a random data matrix of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Determine the shape of the new 3D array
num_matrices = 300
window_size = 10000
num_features = 50

# Reshape the data into a 3D array
Dc = data.reshape(num_matrices, window_size, num_features)

# Check the shape of the new array
print(Dc.shape)  # Output should be (300, 10000, 50)


import numpy as np

# Generate a sample 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array of shape (300, 10000, 50)
# Each group of 10000 rows forms one matrix
D = data.reshape(300, 10000, 50)

# Verify the shape of the new 3D array
print(D.shape)  # Expected output: (300, 10000, 50)

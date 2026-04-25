
import numpy as np

# Generate a sample matrix of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data
result = data.reshape(300, 10000, 50)

# Verify the shape of the new 3D array
print(result.shape)  # Output: (300, 10000, 50)

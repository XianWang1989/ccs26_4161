
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
D = data.reshape(300, 10000, 50)

# Verify the shape of the new 3D array
print(D.shape)  # Should output (300, 10000, 50)

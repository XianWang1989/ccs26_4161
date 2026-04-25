
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
# This will create an array of shape (300, 10000, 50)
Dc = data.reshape(300, 10000, 50)

# Verify the shapes
print("Shape of 3D matrix:", Dc.shape)  # Should output (300, 10000, 50)

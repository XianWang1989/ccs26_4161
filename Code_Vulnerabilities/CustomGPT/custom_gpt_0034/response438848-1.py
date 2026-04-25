
import numpy as np

# Create a sample 2D array of size 3000000x50
data = np.random.randn(3000000, 50)

# Reshape the array into 3D: (300, 10000, 50)
data_3d = data.reshape(300, 10000, 50)

# Print the shape to verify
print(data_3d.shape)  # Output should be (300, 10000, 50)

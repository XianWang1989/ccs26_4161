
import numpy as np

# Create a sample 2D array with shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data to (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the new 3D array
print(reshaped_data.shape)  # Output: (300, 10000, 50)

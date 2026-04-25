
import numpy as np

# Generate a random 2D array
data = np.random.randn(3000000, 50)

# Reshape the 2D array into a 3D array
# New shape is (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape
print(reshaped_data.shape)  # Output: (300, 10000, 50)

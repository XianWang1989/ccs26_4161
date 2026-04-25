
import numpy as np

# Create a sample 2D array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the 2D array into a 3D array
# The first dimension will be 300, the second will be 10000, and the third remains 50
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the reshaped array
print(reshaped_data.shape)  # Output: (300, 10000, 50)


import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data to create a 3D array
# The new shape will be (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(reshaped_data.shape)  # Output: (300, 10000, 50)

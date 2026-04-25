
import numpy as np

# Create a random matrix of size (3000000, 50)
data = np.random.randn(3000000, 50)

# We know we want to reshape this into 300 matrices of size (10000, 50)
new_shape = (300, 10000, 50)

# Reshape the original data directly
reshaped_data = data.reshape(new_shape)

# Confirm the shape of the new 3D array
print(reshaped_data.shape)  # Output should be (300, 10000, 50)

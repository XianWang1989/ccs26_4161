
import numpy as np

# Create a random 2D array with specified dimensions
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
# The first dimension will have 300 matrices, each of size 10000x50
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the reshaped data
print(reshaped_data.shape)  # Output should be (300, 10000, 50)

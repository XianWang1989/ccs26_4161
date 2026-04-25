
import numpy as np

# Create a random 2D array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the array into a 3D array
# The new shape will be (300, 10000, 50)
data_reshaped = data.reshape((300, 10000, 50))

# Verify the shape of the new array
print(data_reshaped.shape)

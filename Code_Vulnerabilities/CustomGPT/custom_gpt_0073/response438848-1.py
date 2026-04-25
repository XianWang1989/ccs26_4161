
import numpy as np

# Create a random 2D array of size 3000000x50
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array: (300, 10000, 50)
reshaped_data = data.reshape((300, 10000, 50))

# Check the shape of the new array
print(reshaped_data.shape)  # Output: (300, 10000, 50)

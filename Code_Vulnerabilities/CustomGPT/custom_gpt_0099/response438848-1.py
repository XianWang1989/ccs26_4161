
import numpy as np

# Generate a random matrix of size 3000000x50
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array with shape (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Print the shape of the new 3D array
print(reshaped_data.shape)


import numpy as np

# Create a random matrix of size 3000000 x 50
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array with shape (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Confirm the shape of the new array
print(reshaped_data.shape)  # Output: (300, 10000, 50)

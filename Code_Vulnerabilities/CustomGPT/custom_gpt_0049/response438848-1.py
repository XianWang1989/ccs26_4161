
import numpy as np

# Create a random 2D array
data = np.random.randn(3000000, 50)

# Reshape the data into the desired 3D shape
# Here, we use (300, 10000, 50) to represent 300 matrices of size 10000x50
reshaped_data = data.reshape(300, 10000, 50)

# Check the shape of the reshaped_data
print(reshaped_data.shape)  # Output: (300, 10000, 50)

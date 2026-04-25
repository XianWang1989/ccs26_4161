
import numpy as np

# Create a random array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array with the desired shape (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(reshaped_data.shape)  # Output should be (300, 10000, 50)


import numpy as np

# Generate a random array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
reshaped_data = data.reshape(300, 10000, 50)

# Confirm the shape of the new array
print(reshaped_data.shape)  # Should output: (300, 10000, 50)

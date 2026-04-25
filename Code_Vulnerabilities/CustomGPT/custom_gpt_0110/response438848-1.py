
import numpy as np

# Create a random 2D array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array of shape (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the new 3D array
print(reshaped_data.shape)  # Should print (300, 10000, 50)

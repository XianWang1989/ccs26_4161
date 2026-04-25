
import numpy as np

# Generate a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array with shape (300, 10000, 50)
# Here, we want 300 blocks of shape (10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

print(reshaped_data.shape)  # This should print (300, 10000, 50)

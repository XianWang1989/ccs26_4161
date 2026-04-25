
import numpy as np

# Create a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array with shape (300, 10000, 50)
D_reshaped = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(D_reshaped.shape)

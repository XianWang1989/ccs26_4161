
import numpy as np

# Create a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
D = data.reshape(300, 10000, 50)

# Check the shapes
print("Shape of original data:", data.shape)
print("Shape of reshaped data:", D.shape)

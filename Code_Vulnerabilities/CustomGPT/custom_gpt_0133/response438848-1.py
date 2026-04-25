
import numpy as np

# Create a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data directly into a 3D array. 
# The new shape should be (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

print(reshaped_data.shape)  # Output should be (300, 10000, 50)

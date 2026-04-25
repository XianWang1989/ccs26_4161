
import numpy as np

# Create a random 2D array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the 2D array into a 3D array of shape (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Now reshaped_data has the desired shape
print(reshaped_data.shape)  # Output should be: (300, 10000, 50)


import numpy as np

# Create a random 2D array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array (300, 10000, 50)
data_reshaped = data.reshape(300, 10000, 50)

# Print the shape to verify
print(data_reshaped.shape)  # Output: (300, 10000, 50)


import numpy as np

# Create a random 2D array of size 3000000 x 50
data = np.random.randn(3000000, 50)

# Reshape the data into 3D array of size (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape
print(reshaped_data.shape)  # Output should be (300, 10000, 50)

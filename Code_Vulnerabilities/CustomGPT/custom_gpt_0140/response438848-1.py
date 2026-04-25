
import numpy as np

# Create a random 2D array of size 3000000x50
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array of size 300x10000x50
# Make sure total elements match: 3000000 == 300 * 10000
data_3d = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(data_3d.shape)  # Output should be (300, 10000, 50)


import numpy as np

# Generate a sample 2D array of size 3000000 x 50
data = np.random.randn(3000000, 50)

# Reshape the 2D array into a 3D array of size 300 x 10000 x 50
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(reshaped_data.shape)

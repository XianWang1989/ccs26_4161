
import numpy as np

# Create a sample 2D array
data = np.random.randn(3000000, 50)

# Reshape the data array into a 3D array
# (300, 10000, 50) where 300 is the number of matrices
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the reshaped array
print(reshaped_data.shape)  # Output should be (300, 10000, 50)

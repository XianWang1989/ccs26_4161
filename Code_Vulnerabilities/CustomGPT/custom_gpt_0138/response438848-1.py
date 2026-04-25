
import numpy as np

# Create a random dataset
data = np.random.randn(3000000, 50)

# Reshape the data into the desired 3D shape
# We want 300 arrays of 10000x50
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(reshaped_data.shape)  # Output should be (300, 10000, 50)

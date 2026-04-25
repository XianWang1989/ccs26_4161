
import numpy as np

# Step 1: Generate the original data
data = np.random.randn(3000000, 50)

# Step 2: Reshape the data into a 3D array
# We want 300 arrays of shape (10000, 50)
# The reshape method requires the total number of elements to remain constant
data_3d = data.reshape(300, 10000, 50)

# Optionally: Verify the shape of the new array
print("Shape of the 3D array:", data_3d.shape)

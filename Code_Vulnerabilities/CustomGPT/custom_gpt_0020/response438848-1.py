
import numpy as np

# Step 1: Create a 2D array
data = np.random.randn(3000000, 50)

# Step 2: Reshape the 2D array into a 3D array
# Here we want a 3D array of shape (300, 10000, 50)
data_3d = data.reshape(300, 10000, 50)

# Verify the shape of the new 3D array
print("Shape of 3D array:", data_3d.shape)

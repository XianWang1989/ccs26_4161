
import numpy as np

# Step 1: Create a random 2D array
data = np.random.randn(3000000, 50)

# Step 2: Reshape the array into 3D
# We want to create 300 matrices of size 10000x50
# Use the reshape method
result = data.reshape(300, 10000, 50)

# Step 3: Verify the shape of the resulting array
print("Shape of the resulting 3D array:", result.shape)

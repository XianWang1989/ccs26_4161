
import numpy as np

# Create a random 2D array of size 3000000x50
data = np.random.randn(3000000, 50)

# Check the shape of the original data
print("Original shape:", data.shape)

# Reshape the data into a 3D array where the first dimension is 300, 
# the second dimension is 10000, and the third dimension is 50.
Dc = data.reshape(300, 10000, 50)

# Check the shape of the new 3D array
print("New shape:", Dc.shape)

# You can access any of the 300 matrices like this:
print("First 10000x50 matrix:\n", Dc[0])


import numpy as np

# Assuming you have your 2D data
data = np.random.randn(3000000, 50)

# Reshape the array to the desired 3D shape
# Here we want 300 matrices of size 10000x50
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape
print(reshaped_data.shape)  # Should output (300, 10000, 50)

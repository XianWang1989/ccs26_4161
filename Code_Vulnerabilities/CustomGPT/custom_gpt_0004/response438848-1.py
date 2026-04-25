
import numpy as np

# Create a random 2D array
data = np.random.randn(3000000, 50)

# Reshape into 3D array
# New shape will be (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the new shape
print(reshaped_data.shape)

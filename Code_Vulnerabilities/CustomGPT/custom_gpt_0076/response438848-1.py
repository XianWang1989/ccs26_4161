
import numpy as np

# Generate the initial data
data = np.random.randn(3000000, 50)

# Reshape the data to the desired 3D shape
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape
print(reshaped_data.shape)  # Should print (300, 10000, 50)

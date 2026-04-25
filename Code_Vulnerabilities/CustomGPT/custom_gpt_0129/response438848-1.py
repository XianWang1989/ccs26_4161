
import numpy as np

# Create an example data array
data = np.random.randn(3000000, 50)

# Reshape the data into 3D array
# Here, the new shape is (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the reshaped data
print("Shape of the reshaped data:", reshaped_data.shape)

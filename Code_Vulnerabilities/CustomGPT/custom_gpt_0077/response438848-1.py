
import numpy as np

# Create a sample data array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into the required 3D shape (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Check the shape of the new array
print(reshaped_data.shape)


import numpy as np

# Create a sample data array
data = np.random.randn(3000000, 50)

# Reshape the data into the desired 3D array
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the reshaped array
print(reshaped_data.shape)  # Should output: (300, 10000, 50)

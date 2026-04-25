
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
# New shape: (300, 10000, 50)
three_d_array = data.reshape(300, 10000, 50)

# Verify the shape of the resulting 3D array
print(three_d_array.shape)  # Should output: (300, 10000, 50)

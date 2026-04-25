
import numpy as np

# Generate the original data
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
data_reshaped = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(data_reshaped.shape)  # Output should be (300, 10000, 50)

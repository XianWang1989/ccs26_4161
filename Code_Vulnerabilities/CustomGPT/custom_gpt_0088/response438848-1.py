
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
# Here, we reshape to (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

print(reshaped_data.shape)  # This should output (300, 10000, 50)

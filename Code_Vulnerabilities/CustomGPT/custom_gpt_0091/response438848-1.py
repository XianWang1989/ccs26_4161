
import numpy as np

# Generate random data of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into 300 matrices of shape (10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Check the shape of the new array
print(reshaped_data.shape)  # Should output (300, 10000, 50)

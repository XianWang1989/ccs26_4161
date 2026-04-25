
import numpy as np

# Generate the original data
data = np.random.randn(3000000, 50)

# Reshape the data into 300 (10000, 50) matrices
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(reshaped_data.shape)  # Output should be (300, 10000, 50)

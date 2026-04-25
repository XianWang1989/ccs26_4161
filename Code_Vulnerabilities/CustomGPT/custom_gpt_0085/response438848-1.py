
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data
# New shape will be (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape
print(reshaped_data.shape)  # Output should be (300, 10000, 50)


import numpy as np

# Create a sample 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the array to (300, 10000, 50)
# Ensure that the original array size matches the new shape
# 300 * 10000 * 50 = 3000000
reshaped_data = data.reshape(300, 10000, 50)

print(reshaped_data.shape)  # Output should be (300, 10000, 50)


import numpy as np

# Generate a sample 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the array to (300, 10000, 50)
# Here, we are splitting the original array into 300 matrices of shape (10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the new shape
print(reshaped_data.shape)  # This should output (300, 10000, 50)

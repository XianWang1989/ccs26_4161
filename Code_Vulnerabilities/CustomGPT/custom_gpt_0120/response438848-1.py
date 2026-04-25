
import numpy as np

# Generate a sample 2D array
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
# Here, we want 300 matrices of shape (10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the new shape
print(reshaped_data.shape)  # Output: (300, 10000, 50)

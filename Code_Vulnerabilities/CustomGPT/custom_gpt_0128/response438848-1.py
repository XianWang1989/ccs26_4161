
import numpy as np

# Generate a random 2D array with shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the array directly into the desired shape (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the reshaped array
print(reshaped_data.shape)  # Output should be (300, 10000, 50)

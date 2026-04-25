
import numpy as np

# Generate a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the array to (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Print the shape to confirm
print(reshaped_data.shape)

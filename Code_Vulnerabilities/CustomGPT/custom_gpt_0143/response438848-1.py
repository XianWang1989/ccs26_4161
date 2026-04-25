
import numpy as np

# Generate a random matrix of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data to (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Print the shape of the new array to verify
print(reshaped_data.shape)

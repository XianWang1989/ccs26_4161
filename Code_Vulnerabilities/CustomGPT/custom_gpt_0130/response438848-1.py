
import numpy as np

# Create a random 2D array of size 3000000x50
data = np.random.randn(3000000, 50)

# Reshape the array to shape (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Example check: print the shape of reshaped_data
print(reshaped_data.shape)  # Output should be (300, 10000, 50)

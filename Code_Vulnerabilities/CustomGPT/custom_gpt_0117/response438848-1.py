
import numpy as np

# Create a random 2D array
data = np.random.randn(3000000, 50)

# Reshape the data to the desired shape
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape of the new array
print(reshaped_data.shape)  # Output: (300, 10000, 50)

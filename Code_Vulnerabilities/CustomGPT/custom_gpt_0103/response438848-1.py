
import numpy as np

# Create a sample 2D array
data = np.random.randn(3000000, 50)

# Reshape the data from (3000000, 50) to (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Check the shape of the new array
print(reshaped_data.shape)  # Output: (300, 10000, 50)

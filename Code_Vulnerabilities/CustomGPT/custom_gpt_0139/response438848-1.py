
import numpy as np

# Create a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshaping the array to (300, 10000, 50)
# You need to ensure that the total number of elements remains the same
# 3000000 = 300 * 10000
reshaped_data = data.reshape((300, 10000, 50))

# Check the shape of the new array
print(reshaped_data.shape)  # Output: (300, 10000, 50)

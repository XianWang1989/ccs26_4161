
import numpy as np

# Generate random data with the shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into (300, 10000, 50)
# This assumes the total number of elements matches: 300 * 10000 * 50 = 3000000
reshaped_data = data.reshape(300, 10000, 50)

# Display the shape of the new array to confirm
print(reshaped_data.shape)  # Output should be (300, 10000, 50)

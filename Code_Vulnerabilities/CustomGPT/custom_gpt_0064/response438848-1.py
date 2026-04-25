
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data
# We need to ensure that the total number of elements remains the same.
reshaped_data = data.reshape(300, 10000, 50)

# Verifying the shape of the new array
print(reshaped_data.shape)  # Output should be (300, 10000, 50)

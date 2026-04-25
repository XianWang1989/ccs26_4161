
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data into the desired shape (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Print the shape to verify
print(reshaped_data.shape)

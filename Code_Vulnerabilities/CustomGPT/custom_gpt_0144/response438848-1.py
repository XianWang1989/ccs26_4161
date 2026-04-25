import numpy as np

# Create the original data
data = np.random.randn(3000000, 50)

# Reshape into 300 chunks of 10000x50
reshaped_data = data.reshape(300, 10000, 50)

print(reshaped_data.shape)  # Output: (300, 10000, 50)

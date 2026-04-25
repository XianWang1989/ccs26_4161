
import numpy as np

# Create a random data array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Output the shape to verify
print(reshaped_data.shape)  # Should output: (300, 10000, 50)

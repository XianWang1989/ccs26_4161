
import numpy as np

# Create a random array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the array into (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Output shape to verify
print(reshaped_data.shape)

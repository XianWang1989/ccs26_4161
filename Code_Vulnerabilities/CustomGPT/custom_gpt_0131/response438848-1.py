
import numpy as np

# Create a random data array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a shape of (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Let's print the shape of the reshaped data to confirm
print(reshaped_data.shape)  # Should output (300, 10000, 50)

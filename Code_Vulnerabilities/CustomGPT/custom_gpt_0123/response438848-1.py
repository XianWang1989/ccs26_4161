
import numpy as np

# Create random data of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data to (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Check the shape of the reshaped data
print(reshaped_data.shape)  # Should print (300, 10000, 50)

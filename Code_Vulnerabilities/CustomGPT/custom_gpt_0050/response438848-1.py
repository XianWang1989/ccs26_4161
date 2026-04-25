
import numpy as np

# Create a random array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into (300, 10000, 50)
data_reshaped = data.reshape(300, 10000, 50)

# Print the shape of the reshaped data to verify
print(data_reshaped.shape)

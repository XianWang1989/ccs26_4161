
import numpy as np

# Generate a sample array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data to (300, 10000, 50)
data_3d = data.reshape(300, 10000, 50)

print("New shape of the array:", data_3d.shape)

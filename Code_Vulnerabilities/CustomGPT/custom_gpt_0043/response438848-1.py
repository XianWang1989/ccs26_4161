
import numpy as np

# Generating a sample 2D array with size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data directly into a 3D array with shape (300, 10000, 50)
data_reshaped = data.reshape(300, 10000, 50)

# Check the shape of the new array
print(data_reshaped.shape)  # Output will be (300, 10000, 50)

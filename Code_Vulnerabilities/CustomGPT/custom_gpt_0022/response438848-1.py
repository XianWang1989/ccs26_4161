
import numpy as np

# Generating a sample 2D array
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
reshaped_data = data.reshape(300, 10000, 50)

# Print the shape of the reshaped array to verify
print(reshaped_data.shape)

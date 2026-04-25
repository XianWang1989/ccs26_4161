
import numpy as np

# Create a random numpy array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array of shape (300, 10000, 50)
# (3000000 / 10000 = 300)
reshaped_data = data.reshape(300, 10000, 50)

# Print the shapes to verify
print('Original shape:', data.shape)
print('Reshaped shape:', reshaped_data.shape)

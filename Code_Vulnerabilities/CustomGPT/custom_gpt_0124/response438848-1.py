
import numpy as np

# Create a sample 2D array
data = np.random.randn(3000000, 50)

# Reshape the 2D array into a 3D array
# The new shape is (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

print("Original shape:", data.shape)
print("New shape:", reshaped_data.shape)

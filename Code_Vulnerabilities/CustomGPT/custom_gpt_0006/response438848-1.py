
import numpy as np

# Generate sample data
data = np.random.randn(3000000, 50)

# Desired shape
num_windows = 300
window_size = 10000

# Reshape the data into the desired 3D shape
reshaped_data = data.reshape(num_windows, window_size, -1)

# Verify the shape of the new array
print(reshaped_data.shape)  # Should output: (300, 10000, 50)

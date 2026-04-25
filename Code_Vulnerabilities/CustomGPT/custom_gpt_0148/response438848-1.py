
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data to create a 3D array
num_windows = 300  # Number of windows
window_size = 10000  # Size of each window
reshaped_data = data.reshape(num_windows, window_size, -1)  # The last dimension is automatically set to 50

# Verify the shape
print(reshaped_data.shape)  # Should output (300, 10000, 50)


import numpy as np

# Generating a sample 2D array
data = np.random.randn(3000000, 50)

# Parameters
num_windows = 300  # Number of 10000x50 matrices
window_size = 10000  # Size of each window

# Reshape the data into 3D array
array_3d = data.reshape(num_windows, window_size, -1)

# Verifying the shape of the resulting 3D array
print(array_3d.shape)  # Should output (300, 10000, 50)

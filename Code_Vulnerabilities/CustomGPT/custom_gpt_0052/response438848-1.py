
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Define parameters
lw = 10000  # length of each window
num_windows = data.shape[0] // lw  # calculate number of windows

# Reshape the data into a 3D array
Dc = data.reshape(num_windows, lw, -1)

# Verify the shape
print(Dc.shape)  # Should output (300, 10000, 50)

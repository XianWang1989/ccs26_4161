
import numpy as np

# Generate random data (3000000x50)
data = np.random.randn(3000000, 50)

# Number of windows and window length
num_windows = 300  # We want 300 matrices
window_length = 10000  # Each matrix will be of size 10000x50

# Reshape the data directly into the desired format
# You can reshape data as (num_windows, window_length, num_features)
Dc = data.reshape(num_windows, window_length, -1)

# Verify the shape of the new 3D array
print(Dc.shape)  # Should output (300, 10000, 50)

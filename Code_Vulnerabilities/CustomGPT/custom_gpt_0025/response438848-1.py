
import numpy as np

# Generate a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Number of windows and length of each window
num_windows = 300
window_length = 10000

# Reshaping the data into a 3D array
# The shape should be (300, 10000, 50)
D_reshaped = data.reshape(num_windows, window_length, -1)

# Verify the shape of the new array
print(D_reshaped.shape)  # Output: (300, 10000, 50)


import numpy as np

# Generate dummy data
data = np.random.randn(3000000, 50)

# Reshape the data
lw = 10000  # length of each window
num_windows = data.shape[0] // lw  # number of windows
Dc = data.reshape(num_windows, lw, -1)  # reshape into 3D array

# Display shape of the new array to confirm
print(Dc.shape)  # Expected output: (300, 10000, 50)

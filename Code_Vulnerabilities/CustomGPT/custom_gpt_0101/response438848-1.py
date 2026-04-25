
import numpy as np

data = np.random.randn(3000000, 50)
lw = 10000  # Length of each window
l = data.shape[0] // lw  # Number of windows

# Reshape data into 3D array
D = data.reshape(l, lw, -1)

# Example output
print(D.shape)  # Should output (300, 10000, 50)

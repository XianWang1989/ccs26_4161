
import numpy as np

# Generate a random 2D array of shape (3000000, 50)
data = np.random.randn(3000000, 50)

# Define parameters
ts = 50           # Number of features (columns)
lw = 10000       # Length of each window
l = data.shape[0] // lw  # Number of windows (300 in this case)

# Initialize the 3D array
Dc = np.zeros((l, lw, ts))

# Fill the 3D array
for i in range(l):
    Dc[i] = data[(lw * i):(lw * (i + 1)), :]

# Now Dc has the shape (300, 10000, 50)
print(Dc.shape)  # Output should be (300, 10000, 50)

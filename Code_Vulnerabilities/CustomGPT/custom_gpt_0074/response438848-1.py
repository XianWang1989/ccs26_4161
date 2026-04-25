
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)
D = np.matrix.conjugate(data)

# Define number of time series and window length
ts = 50
lw = 10000  # length of each window 

# Calculate number of windows
l = len(data) // lw

# Initialize the 3D array
Dc = np.zeros((l, lw, ts))

# Fill the 3D array with slices of the original data
for i in range(l):
    Dc[i] = D[(lw * i):(lw * (i + 1)), :]

# Now Dc will hold the split matrices as desired

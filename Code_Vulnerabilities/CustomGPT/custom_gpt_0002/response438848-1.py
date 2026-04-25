
import numpy as np

# Create the original 2D array
data = np.random.randn(3000000, 50)
ts = 50  # number of time series
lw = 10000  # length of each window 

# Calculate the number of windows
l = len(data) // lw

# Initialize the new 3D array
Dc = np.zeros((l, lw, ts))

# Fill the 3D array
for i in range(l):
    Dc[i] = data[(lw * i):(lw * (i + 1)), :]

print(Dc.shape)  # Output should be (300, 10000, 50)

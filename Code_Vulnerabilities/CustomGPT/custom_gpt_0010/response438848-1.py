
import numpy as np

# Create a random 2D array of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
# Here, we reshape the data directly
D = data.reshape((300, 10000, 50))

# Alternatively, if you want to ensure the data is split correctly
l = 300  # Number of 3D matrices
lw = 10000  # Length of each window

# Initialize an empty 3D array
Dc = np.zeros((l, lw, 50))

# Fill the 3D array
for i in range(l):
    Dc[i] = data[(lw * i):(lw * (i + 1))]

# Now Dc will be your desired 3D array
